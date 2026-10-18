import argparse

def main():
    parser = argparse.ArgumentParser(
        description="A Personal Security Utility"
    )
    subparser = parser.add_subparsers(
        dest="command",
        required=True
    )

    # Add subcommands here
    f_import = subparser.add_parser(
        "-i", "--import",
        help="Import the file or folder"
    )

    f_export = subparser.add_parser(
        "-e", "--export",
        help="Export the file or folder",
        default="README"
    )

    options = subparser.add_parser(
        "-o", "--options",
        help="See more options for the utility"
    )

    _help = subparser.add_parser(
        "-h", "--help",
        help="Display help information"
    )


    args = parser.parse_args()

    if args.command == "import":
        print("Importing file or folder...")
        # Add import functionality here\
    elif args.command == "export":
        print("Exporting file or folder...")
        # Add export functionality here
    elif args.command == "options":
        print("Displaying more options...")
        # Add options functionality here
    elif args.command == "help":
        parser.print_help()
    else:
        print("Invalid command. Use -h for help.")

if __name__ == "__main__":
    main()