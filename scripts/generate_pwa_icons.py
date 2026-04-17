#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate PWA icons from SVG favicon
Creates 192x192 and 512x512 PNG icons for PWA manifest
"""

import os
import base64

# Simple Python script to create minimal PNG icons
# Using a basic solid color + text approach without external dependencies

def create_simple_png(size, output_path):
    """Create a simple green square PNG icon using raw bytes"""
    # This creates a minimal valid PNG
    import struct
    import zlib
    
    width = height = size
    
    # Create image data (RGBA)
    # Green background (#22C55E) with white JSON text
    pixels = []
    for y in range(height):
        row = []
        for x in range(width):
            # Background color: #22C55E (green)
            r, g, b, a = 34, 197, 94, 255
            
            # Create a simple border effect
            margin = size // 8
            if x < margin or x >= width - margin or y < margin or y >= height - margin:
                r, g, b = 22, 163, 74  # Darker green border
            
            # White center dot pattern (simplified JSON brackets)
            center_x, center_y = width // 2, height // 2
            dot_r = size // 6
            
            # Draw { symbol representation
            dist = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
            
            row.extend([r, g, b, a])
        pixels.append(row)
    
    # PNG file structure
    def pack_chunk(chunk_type, data):
        chunk_len = len(data)
        chunk_data = chunk_type + data
        crc = zlib.crc32(chunk_data) & 0xFFFFFFFF
        return struct.pack('>I', chunk_len) + chunk_data + struct.pack('>I', crc)
    
    # PNG signature
    signature = b'\x89PNG\r\n\x1a\n'
    
    # IHDR chunk
    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)  # 8-bit RGB
    ihdr = pack_chunk(b'IHDR', ihdr_data)
    
    # Create RGB image data
    raw_data = b''
    for y in range(height):
        raw_data += b'\x00'  # Filter type: None
        for x in range(width):
            # Background color: #22C55E (green)
            r, g, b = 34, 197, 94
            
            # Rounded corner effect
            margin = size // 8
            inner_size = size - 2 * margin
            rx = x - margin
            ry = y - margin
            corner_r = inner_size // 4
            
            in_rect = (margin <= x < width - margin) and (margin <= y < height - margin)
            if not in_rect:
                r, g, b = 19, 28, 46  # Dark background outside
            else:
                r, g, b = 34, 197, 94  # Green
                
                # White lines pattern (JSON-like)
                line_w = max(2, size // 64)
                third = inner_size // 3
                
                # Top white line
                if abs(ry - third) <= line_w and third // 2 <= rx <= inner_size - third // 2:
                    r, g, b = 255, 255, 255
                
                # Middle white line
                if abs(ry - inner_size // 2) <= line_w and third // 4 <= rx <= inner_size - third // 4:
                    r, g, b = 255, 255, 255
                
                # Bottom white line
                if abs(ry - (inner_size - third)) <= line_w and third // 2 <= rx <= inner_size - third // 2:
                    r, g, b = 255, 255, 255
            
            raw_data += struct.pack('BBB', r, g, b)
    
    # IDAT chunk (compressed)
    compressed = zlib.compress(raw_data)
    idat = pack_chunk(b'IDAT', compressed)
    
    # IEND chunk
    iend = pack_chunk(b'IEND', b'')
    
    with open(output_path, 'wb') as f:
        f.write(signature + ihdr + idat + iend)
    
    print(f'Created {output_path} ({size}x{size})')

def main():
    images_dir = r'd:\网站开发-json\images'
    
    create_simple_png(192, os.path.join(images_dir, 'icon-192.png'))
    create_simple_png(512, os.path.join(images_dir, 'icon-512.png'))
    
    print('PWA icons created successfully!')

if __name__ == '__main__':
    main()
