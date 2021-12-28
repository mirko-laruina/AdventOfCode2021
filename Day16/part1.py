#!/bin/env python3

class PacketOperator:
    def __init__(self, bits) -> None:
        self.length_type_id = int(bits[0], 2)
        # print("Packet operator:", bits)
        # print("Length type:", self.length_type_id)
        self.length = 1
        self.inner_packets = []
        if self.length_type_id == 0 :
            inner_packets_len = int(bits[1:16], 2)
            self.length += 15
            # print("Inner packet len:", inner_packets_len)
            remaining_bits = bits[16:]
            remaining_len = inner_packets_len
            while remaining_len > 0:
                # print("----------------------")
                # print(f"Remaining bits: ", len(remaining_bits), remaining_bits, remaining_len)
                inner_packet = Packet(remaining_bits)
                # print(f"Packet length:  {inner_packet.length}")
                #print("----------------------")
                self.inner_packets.append(inner_packet)
                remaining_len -= inner_packet.length
                remaining_bits = remaining_bits[inner_packet.length:]
            self.length += inner_packets_len
        else:
            num_inner_packets = int(bits[1:12], 2)
            remaining_bits = bits[12:]
            self.length += 11
            inner_packets_len = 0
            # print("Inner packets num:",num_inner_packets)
            while num_inner_packets > 0:
                # print("----------------------")
                # print(f"Remaining bits: ", len(remaining_bits), remaining_bits)
                inner_packet = Packet(remaining_bits)
                # print(f"Packet length:  {inner_packet.length}")
                # print("----------------------")
                self.inner_packets.append(inner_packet)
                num_inner_packets -= 1
                remaining_bits = remaining_bits[inner_packet.length:]
                inner_packets_len += inner_packet.length
            # print("READ PACKETS:", self.inner_packets)
            self.length += inner_packets_len
    
    def __repr__(self) -> str:
        return f"{self.inner_packets}"


class Packet :
    def __init__(self, bits) -> None:
        self.version = int(bits[0:3], 2)
        self.type_id = int(bits[3:6], 2)
        self.length = 6
        self.payload = None

        # print("Packet:", bits)
        # print(f"Version: {self.version}. Type: {self.type_id}")
        if self.type_id == 4:
            # print("Literal")
            # it is a literal value
            self.payload, literal_length = Packet.read_literal_value(bits[6:])
            self.length += literal_length
            # print("Literal value:", self.payload)
        else:
            # print("Operator")
            # print("*******************************************")
            # it is an operator
            self.payload, operator_length = Packet.read_operator(bits[6:])
            # print("*******************************************")
            self.length += operator_length

    def read_literal_value(value_bits):
        useful_bits = ''
        bit_counter = 0
        bits = value_bits
        while int(bits[0], 2) == 1:
            bit_counter += 5
            useful_bits += bits[1:5]
            bits = bits[5:]
        useful_bits += bits[1:5]
        return int(useful_bits, 2), bit_counter + 5

    def read_operator(operator_bits):
        operator = PacketOperator(operator_bits)
        return operator, operator.length

    def __repr__(self) -> str:
        return f"version: {self.version} | type {self.type_id} | payload: {self.payload}"
        

def sum_version(packet):
    sum = 0
    if isinstance(packet.payload, PacketOperator):
        for inner in packet.payload.inner_packets:
            sum += sum_version(inner)
    sum += packet.version
    return sum

with open("input.txt") as f:
    line = f.readline().strip()

bits = ''
for char in line:
    bin = format(int(char, 16), "04b")
    bits += bin


packet = Packet(bits)
print(sum_version(packet))


