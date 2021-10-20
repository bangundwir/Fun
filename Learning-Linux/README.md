# Opensource Licensing Models
  - Free Software foundation (FSF)
    - GPL (Linux karnel)
  - Open Source INitiative (OSI)
  - Creative Commons
    - Attribution
    - Share-alike
    - Non-commercial
    - No Derivative Works
    - Public Domain

# Free Software
  - FOSS : Free and Open Source software
  - FLOS : Free/Libre and Open Source Software

# The Linux Oprating System
  - The Linux Ecosystem
    - Linus Torvals
    - Linux
    - Third-party customizations
  - User I/O operations Interpreted by the OS
    - Operating System
    - Storage Device | System access
    - Motherboard | CPU | Memory | Networking
  - The Linux Kernel Is Free
    - Customization
      - Don't like the way it came? Rebuild Linux to taste
    - Flexibility
      - Move drives between manchines; duplicate and share images
    - Virutalization
      - you can freely explore, experiment, and test configurations
    - The Layers of a Linux Distribution
      - The Liux kernel handles system hardware resources on behalf of the OS user
      - A Linux desktop is a software designed to manage graphic interface features like windows, menus, and application controls
      - A Linux distribution will use a specific suite of system tools (like software package managers and process managers)

# Linux Distributions
  - Android (mobile devices)
  - Red hat Enterprise Linux
    - CentOS
  - SUSE
    - Open SUSE
  - Scientific Linux  (science and math)
  - Kali Linux (security)
  - Rapbian (mini architectures)
  - ubuntu (all-round)
  - Mint (consumer-griendly)
  - Virtual Machines
  - Cloud Computing

# Destribution Families
  - Debian
    - Ubuntu, Mint, and Kali Linux
  - Red Hat Enterprise Linux
    - CentOS and Fedora
  - SUSE
    - OpenSUSE
  - Arch Linux
    - LinHES and Manjaro
    

# Configuring the Linux Environment
 - Multi-user Systems
  - Admin Access
  - Web Root Acess
  - Database Access

 
# Command 
  - CTRL + ALT +T = Membuka Terminal 

# The LInux Filesystem Hierarchy Standard
  - Root-Level Directories
    - /bin   Binary files for (single user mode) system commands
    - /sbin  Binary files for (multi-user) system commands
    - /boot  Linux images and boot configuration files
    - /dev   Pseudo files representing devices
    - /etc   Configuration files
    - /home  User files
    - /lib   Software library dependencies
    - /root  Root user files
    - /user  Additional binaries
    - /var   Updating files: logs, application data, cache

  - Pseudo File Directories
    - /proc   Files representing running stystem processes
    - /dev    Pseudo files representing devices
    - /sys    Data on system and kernel resources

# Managing Linux Environments
  - locale 
  - localectl status
  - pwd
  - env
  - timedatectl
  - timedatectl list-timezones | grep -i america
  - timedatectl list-timezones | grep -i jakarta  

# Managing System Hardware
  - df -ht ext4
  - lsblk | grep sd
  - dmesg
  - lshw 
  - lshw | less

# Linux Desktop Aplication
  - apt list --all-versions | wc
  - apt search business card | cat
  - apt show glabels

# Working with the Linux Server
  - wget -c https://github.com/prasmussen/gdrive/releases/download/2.1.1/gdrive_2.1.1_linux_amd64.tar.gz -O - | sudo tar -xz

