def filter_comment_lines(src_file, dest_file):
    with open(src_file, "r") as infile, open(dest_file, "w") as outfile:
        for line in infile:
            if not line.startswith('#'):
                outfile.write(line)
        print("Filtering of comment lines succesful, check the contents of destination file")
src=input("Enter the name of the source file: ")
dest=input("Enter the name of the destination file: ")
filter_comment_lines(src,dest)