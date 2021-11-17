# Solution

- we are given a jpg-file with a cat in the picure! No hints there
- lets look into the metadata
- running $ **exiftool cat.jpg** gives us:

      ExifTool Version Number         : 12.30
      File Name                       : cat.jpg
      Directory                       : .
      File Size                       : 858 KiB
      File Modification Date/Time     : 2021:11:16 20:13:40-05:00
      File Access Date/Time           : 2021:11:16 20:13:48-05:00
      File Inode Change Date/Time     : 2021:11:16 20:13:44-05:00
      File Permissions                : -rw-r--r--
      File Type                       : JPEG
      File Type Extension             : jpg
      MIME Type                       : image/jpeg
      JFIF Version                    : 1.02
      Resolution Unit                 : None
      X Resolution                    : 1
      Y Resolution                    : 1
      Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
      Copyright Notice                : PicoCTF
      Application Record Version      : 4
      XMP Toolkit                     : Image::ExifTool 10.80
      License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
      Rights                          : PicoCTF
      Image Width                     : 2560
      Image Height                    : 1598
      Encoding Process                : Baseline DCT, Huffman coding
      Bits Per Sample                 : 8
      Color Components                : 3
      Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
      Image Size                      : 2560x1598
      Megapixels                      : 4.1

- That license looks somewhat suspicious, base64!
- typing the following into terminal to decrypt:

      cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9 | base64 -d
      
- YUUUPP!
