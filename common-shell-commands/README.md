# Useful shell commands

## Text Manipulation

* print the first column of the file

        example.txt
        -----------
        1 2 3
        1.1 2.2 3.3

    run

        awk '{print $1}' example.txt

    for columns seperated by `,`

        example.txt
        -----------
        1,2,3
        1.1,2.2,3.3

    use

        awk -F , '{print $1}' example.txt


## Download

* download all files under a directory

        wget -r -np https://docs.python.org/2/library/ 

    `-r` means recursive; `-np` means don't go to parent nodes

