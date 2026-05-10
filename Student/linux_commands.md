### 1. SYSTEM

    $ uname –a                          # Display linux system information
    $ uname –r                          # Display kernel release information (refer uname command in detail)
    $ hostname                          # Show system host name
    $ hostname -i                       # Display the IP address of the host (all options hostname)
    $ uptime                            # Show how long system running + load (learn uptime command)
    $ last reboot                       # Show system reboot history (more examples last command)
    $ cat /etc/redhat_release           # Show which version of redhat installed 
    $ date                              # Show the current date and time (options of date command)
    $ cal                               # Show this month calendar (what more in cal)
    $ w                                 # Display who is online (learn more about w command)
    $ whoami                            # Who you are logged in as (example + sreenshots)
    $ finger user                       # Display information about user (many options of finger command)

### 2. Hardware

    $ dmesg                             # Detected hardware and boot messages (dmesg many more options)
    $ cat /proc/cpuinfo                 # CPU model
    $ cat /proc/meminfo                 # Hardware memory
    $ cat /proc/interrupts              # Lists the number of interrupts per CPU per I/O device
    $ lshw                              # Displays information on hardware configuration of the system
    $ lsblk                             # Displays block device related information in Linux (sudo yum install util-linux-ng)
    $ free -m                           # Used and free memory (-m for MB) (free command in detail)
    $ lspci -tv                         # Show PCI devices (very useful to find vendor ids)
    $ lsusb -tv                         # Show USB devices (read more lsusb options)
    $ lshal                             # Show a list of all devices with their properties 
    $ dmidecode                         # Show hardware info from the BIOS (vendor details)
    $ hdparm -i /dev/sda                # Show info about disk sda 
    $ hdparm -tT /dev/sda               # Do a read speed test on disk sda
    $ badblocks -s /dev/sda             # Test for unreadable blocks on disk sda

### 3. Statistics

    $ top                               # Display and update the top cpu processes (30 example options)
    $ mpstat 1                          # Display processors related statistics (learn mpstat command)
    $ vmstat 2                          # Display virtual memory statistics (very useful performance tool)
    $ iostat 2                          # Display I/O statistics (2sec Intervals) (more examples)
    $ tail -n 500 /var/log/messages     # Last 10 kernel/syslog messages (everyday use tail options)
    $ tcpdump -i eth1                   # Capture all packets flows on interface eth1 (useful to sort network issue)
    $ tcpdump -i eth0 'port 80'         # Monitor all traffic on port 80 ( HTTP )
    $ lsof                              # List all open files belonging to all active processes.(sysadmin favorite command)
    $ lsof -u testuser                  # List files opened by specific user
    $ free –m                           # Show amount of RAM (daily usage command)
    $ watch df –h                       # Watch changeable data continuously(interesting linux command)

### 4. Users

    $ id                                        # Show the active user id with login and group(with screenshot)
    $ last                                      # Show last logins on the system (few more examples)
    $ who                                       # Show who is logged on the system (real user who logged in)
    $ groupadd   admin                          # Add group "admin" (force add existing group)
    $ useradd -c "Sam Tomshi" -g admin -m sam   # Create user "sam" and add to group "admin" (here read all parameter)
    $ userdel sam                               # Delete user sam (force,file removal)
    $ adduser sam                               # Add user "sam" 
    $ usermod                                   # Modify user information (mostly useful for linux system admins)

### 5. File Commands

    $ ls –al                                # Display all information about files/ directories(20 examples)
    $ pwd                                   # Show current directory path(simple but need every day)
    $ mkdir directory-name                  # Create a directory(create mutiple directory)
    $ rm file-name                          # Delete file(be careful of using rm command)
    $ rm -r directory-name                  # Delete directory recursively 
    $ rm -f file-name                       # Forcefully  remove file
    $ rm -rf directory-name                 # Forcefully remove directory recursively
    $ cp file1 file2                        # Copy file1 to file2 (15 cd command examples)
    $ cp -r dir1 dir2                       # Copy dir1 to dir2, create dir2 if it doesn’t  exist
    $ mv file1 file2                        # Move files from one place to another(with 10 examples)
    $ ln –s  /path/to/file-name  link-name  # Create symbolic link to file-name (examples)
    $ touch file                            # Create or update file (timestamp change)
    $ cat > file                            # Place standard input into file (15 cat command examples)
    $ more file                             # Output the contents of file (help display long tail files)
    $ head file                             # Output the first 10 lines of file (with different parameters)
    $ tail file                             # Output the last 10 lines of file (detailed article with tail options)
    $ tail -f file                          # Output the contents of file as it grows starting with the last 10 lines
    $ gpg -c file                           # Encrypt file (how to use gpg)
    $ gpg file.gpg                          # Decrypt file

### 6. Process Related

    $ ps                                # Display your currently active processes (many parameters to learn)
    $ ps aux | grep 'telnet'            # Find all process id related to telnet process
    $ pmap                              # Memory map of process (kernel,user memory etc)
    $ top                               # Display all running processes (30 examples)
    $ kill pid                          # Kill process with mentioned pid id (types of signals)
    $ killall proc                      # Kill all processes named proc
    $ pkill processname                 # Send signal to a process with its name
    $ bg                                # Resumes suspended jobs without bringing them to foreground (bg and fg command)
    $ fg                                # Brings the most recent job to foreground
    $ fg n                              # Brings job n to the foreground

### 7. File Permission Related

    $ chmod octal file-name                     # Change the permissions of file to octal , which can be found separately for user, group and world
                                                # Octal value (more examples)
                                                # 4 - read
                                                # 2 – write
                                                # 1 – execute
    # Example 
    $ chmod 777 /data/test.c                    # Set rwx permission for owner , rwx  permission for group, rwx permission for world
    $ chmod 755 /data/test.c                    # Set rwx permission for owner,rx for group and world
    $ chown owner-user file                     # Change owner of the file (chown more examples)
    $ chown owner-user:owner-group  file-name   # Change owner and group owner of the file
    $ chown owner-user:owner-group directory    # Change owner and group owner of the directory
    # Example 
    $ chown bobbin:linoxide test.txt
    $ ls -l test.txt                            # -rw-r--r-- 1 bobbin linoxide 0 Mar 04 08:56 test.txt


### 8. Network

    $ ifconfig –a                           # Display all network ports and ip address (set mtu and other all options)
    $ ifconfig eth0                         # Display specific  ethernet port ip address and details
    $ ip addr show                          # Display all network interfaces and ip address (available in iproute2 package, more powerful than ifconfig)
    $ ip address add 192.168.0.1 dev eth0   # Set ip address
    $ ethtool eth0                          # Linux tool to show ethernet status (set full duplex , pause parameter)
    $ mii-tool  eth0                        # Linux tool to show  ethernet status (more or like ethtool)
    $ ping host                             # Send echo request to test connection (learn sing enhanced ping tool)
    $ whois domain                          # Get who is information for domain
    $ dig domain                            # Get DNS information for domain (screenshots with other available parameters)
    $ dig  -x host                          # Reverse lookup host 
    $ host google.com                       # Lookup DNS ip address for the name (8 examples of host command)
    $ hostname –i                           # Lookup local ip address (set hostname too)
    $ wget file                             # Download file (very useful other option)
    $ netstat  -tupl                        # Listing all active listening ports(tcp,udp,pid) (13 examples)

### 9. Compression / Archives

    $ tar cf home.tar  home             # Create tar named home.tar containing home/ (11 tar examples)
    $ tar xf file.tar                   # Extract the files from file.tar
    $ tar czf  file.tar.gz  files       # Create a tar with gzip compression
    $ gzip file                         # Compress file and renames it to file.gz (untar gzip file)

### 10. Install Package

    $ rpm -i pkgname.rpm                # Install rpm based package (Installing, Uninstalling, Updating, Querying, Verifying)
    $ rpm -e pkgname                    # Remove package
    # Install from source
    $ ./configure
    $ make
    $ make install (what it is)

### 11. Search

    $ grep pattern files                # Search for pattern in files (you will this command often)
    $ grep  -r pattern dir              # Search recursively for pattern in dir
    $ locate file                       # Find all instances of file
    $ find /home/tom -name 'index*'     # Find files names that start with "index"(10 find examples)
    $ find /home -size +10000k          # Find files larger than 10000k in /home

### 12. Login (ssh and telnet)

    $ ssh user@host                     # Connect to host as user (secure data communication command)
    $ ssh  -p port user@host            # Connect to host using specific port
    $ telnet host                       # Connect to the system using  telnet port
    
### 13. File Transfer

    scp
    $ scp file.txt   server2:/tmp                           # Secure copy file.txt to remote host  /tmp folder
    $ scp nixsavy@server2:/www/*.html   /www/tmp            # Copy *.html files from remote host to current system /www/tmp folder
    $ scp -r nixsavy@server2:/www   /www/tmp                # Copy all files and folders recursively from remote server to the current system /www/tmp folder
    rsync
    $ rsync -a /home/apps /backup/                          # Synchronize source to destination
    $ rsync -avz /home/apps linoxide@192.168.10.1:/backup   # Synchronize files/directories between the local and remote system with compression enabled

### 14. Disk Usage

    $ df –h                             # Show free space on mounted filesystems(commonly used command)
    $ df -i	                            # Show free inodes on mounted filesystems
    $ fdisk -l	                        # Show disks partitions sizes and types(fdisk command output)
    $ du -ah                            # Display disk usage in human readable form (command variations)
    $ du -sh                            # Display total disk usage on the current directory
    $ findmnt                           # Displays target mount point for all filesystem (refer type,list,evaluate output)
    $ mount device-path mount-point     # Mount a device 

### 15. Directory Traverse

    $ cd /test                          # Change to /test directory
    $ cd ..                             # To go up one level of the directory tree(simple & most needed)
    $ cd	                            # Go to $HOME directory