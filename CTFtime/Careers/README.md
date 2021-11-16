# Soultion

- On this page we are supposed to upload our CV, but only txt-files are allowed, and we are supposed to zip the files that are being uploaded

![Screenshot 2021-11-16 at 20 18 35](https://user-images.githubusercontent.com/74051842/142051165-bbc37ba3-d224-4a7a-9eb6-46e629e15904.png)

- The website uses php so we will try to inject some:

![Screenshot 2021-11-16 at 20 36 54](https://user-images.githubusercontent.com/74051842/142053818-954f67ae-26fc-44a7-848d-2fa5fcdeedcc.png)

- and compressing:

![Screenshot 2021-11-16 at 20 37 05](https://user-images.githubusercontent.com/74051842/142053788-8c868870-075f-4a7a-98ab-835b62456091.png)

- going to the page where the file is uploaded will give us the flag

# Takeaways

- php pages can be vulnerable to injections
- zip files might be able breach security measures if an uncompressed file cant
