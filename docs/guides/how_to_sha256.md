
# **How to Use SHA256 on macOS**

## **What is a SHA256 Checksum?**

SHA256 (Secure Hash Algorithm 256-bit) is a cryptographic hash function that generates a unique, fixed-length string for a given file. It's commonly used to:

- Verify file integrity: Ensure a downloaded file hasn’t been tampered with.
- Authenticate downloads: Match the provided checksum with the file's checksum.

---

## **How to Generate a SHA256 Checksum**

1. **Open the Terminal**:
   - Use Spotlight (`Cmd + Space`) to search for "Terminal" and open it.

2. **Navigate to the File Location**:
   - Use the `cd` command to go to the folder containing your file:
     ```bash
     cd /path/to/your/file
     ```

3. **Run the Checksum Command**:
   - Replace `yourfile` with the actual filename:
     ```bash
     shasum -a 256 yourfile
     ```
   - Example output:
     ```
     e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  yourfile
     ```
   - The long string is the file's SHA256 checksum.

4. **Compare Checksum Values**:
   - Match the output with the checksum provided by the file's source to ensure it’s unchanged.

---

## **How to Use a SHA256 Checksum with `curl`**

When downloading files using `curl`, you can verify the integrity of the downloaded file by comparing its checksum with the expected value.

1. **Download the File with `curl`**:
   - Replace `<url>` with the file’s download link:
     ```bash
     curl -O <url>
     ```
     Example:
     ```bash
     curl -O https://example.com/myfile.pkg
     ```

2. **Generate the Checksum**:
   - Run the same command as above to get the checksum of the downloaded file:
     ```bash
     shasum -a 256 myfile.pkg
     ```

3. **Verify the Checksum**:
   - Compare the output of the command with the checksum provided by the file's source. If the checksums match, the file is intact.

---

### **Example Workflow**

1. **Download the file**:
   ```bash
   curl -O https://example.com/software.pkg
   ```
2. **Check the checksum**:
   ```bash
   shasum -a 256 software.pkg
   ```
3. **Compare with the provided checksum**:
   - If the checksum provided is `abc123...`, ensure the output matches:
     ```
     abc123...  software.pkg
     ```