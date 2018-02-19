import Parser
import ParserSettings


class ParserUI:
    def __init__(self):
        self.parser = Parser.Parser()
        self.parser_setting = ParserSettings.ParserSettings()

    def run(self):
        # Attempt to load default parser settings
        try:
            self.parser_setting.read("cfg/default_setting.cfg")
        except FileNotFoundError:
            print("Default settings cannot be found!")
            print("Generating new default settings...\n")
            self.generate_new_default_setting()

        # Prompt user for input
        self.prompt_screen()

    def prompt_screen(self):
        while True:
            print("(L)oad new parser settings")
            print("(S)ave current parser settings")
            print("(E)dit parser settings")
            print("(N)ew parser operation")
            print("(Q)uit")
            user_input = str(input(">"))

            # Load New Parser Settings
            if user_input.lower().strip() == 'l':
                self.load_new_parser_settings()
            # Save Current Parser Settings
            elif user_input.lower().strip() == 's':
                self.save_current_parser_settings()
            # Edit Parser Settings
            elif user_input.lower().strip() == 'e':
                self.edit_parser_operations()
            # New Parser Operation
            elif user_input.lower().strip() == 'n':
                pass
            # Quit
            elif user_input.lower().strip() == 'q':
                break

    def edit_parser_operations(self):
        print("Order logs by? ('query_time', 'lock_time', 'rows_sent', 'rows_examined', 'datetime')")
        user_input = str(input(">"))
        self.parser_setting.order = ParserSettings.sanitize_order(user_input)
        print("Sort by? ('asc', 'desc')")
        user_input = str(input(">"))
        self.parser_setting.sort = ParserSettings.sanitize_sort(user_input)
        print("Default log name (cannot contain characters \ / : * ? \" < > |")
        user_input = str(input(">"))
        self.parser_setting.default_log_name = ParserSettings.sanitize_filename(user_input)
        print("Output query min time (-1 for no checking)")
        user_input = str(input(">"))
        self.parser_setting.output_query_time_min = ParserSettings.sanitize_number(user_input)
        print("Output query max time (-1 for no checking)")
        user_input = str(input(">"))
        self.parser_setting.output_query_time_max = ParserSettings.sanitize_number(user_input)
        print("Output lock min time (-1 for no checking)")
        user_input = str(input(">"))
        self.parser_setting.output_lock_time_min = ParserSettings.sanitize_number(user_input)
        print("Output lock max time (-1 for no checking)")
        user_input = str(input(">"))
        self.parser_setting.output_lock_time_max = ParserSettings.sanitize_number(user_input)
        print("Output rows sent min time (-1 for no checking)")
        user_input = str(input(">"))
        self.parser_setting.output_rows_sent_min = ParserSettings.sanitize_number(user_input)
        print("Output rows sent time (-1 for no checking)")
        user_input = str(input(">"))
        self.parser_setting.output_rows_sent_max = ParserSettings.sanitize_number(user_input)
        print("Output rows examined min time (-1 for no checking)")
        user_input = str(input(">"))
        self.parser_setting.output_rows_examined_min = ParserSettings.sanitize_number(user_input)
        print("Output rows examined max time (-1 for no checking)")
        user_input = str(input(">"))
        self.parser_setting.output_rows_examined_max = ParserSettings.sanitize_number(user_input)
        print("Output datetime min (YYYY-MM-DD)")
        user_input = str(input(">"))
        self.parser_setting.output_datetime_min = ParserSettings.sanitize_datetime(user_input)
        print("Output datetime max (YYYY-MM-DD)")
        user_input = str(input(">"))
        self.parser_setting.output_datetime_max = ParserSettings.sanitize_datetime(user_input)
        print("Output database user (leave blank for no filters)")
        user_input = str(input(">"))
        self.parser_setting.output_database_user = user_input
        print("Output database host (leave blank for no filters)")
        user_input = str(input(">"))
        self.parser_setting.output_database_host = user_input
        print("Output database name (leave blank for no filters)")
        user_input = str(input(">"))
        self.parser_setting.output_database_name = user_input
        print("Display Datetime ? (0 or 1)")
        user_input = str(input(">"))
        self.parser_setting.display_datetime = ParserSettings.sanitize_binary_number(user_input)
        print("Display Database Host? (0 or 1)")
        user_input = str(input(">"))
        self.parser_setting.display_database_host = ParserSettings.sanitize_binary_number(user_input)
        print("Display Time? (0 or 1)")
        user_input = str(input(">"))
        self.parser_setting.display_time = ParserSettings.sanitize_binary_number(user_input)
        print("Display Database? (0 or 1)")
        user_input = str(input(">"))
        self.parser_setting.display_database = ParserSettings.sanitize_binary_number(user_input)
        print("Display Timestamp? (0 or 1)")
        user_input = str(input(">"))
        self.parser_setting.display_timestamp = ParserSettings.sanitize_binary_number(user_input)
        print("Display Statement? (0 or 1)")
        user_input = str(input(">"))
        self.parser_setting.display_statement = ParserSettings.sanitize_binary_number(user_input)

    def load_new_parser_settings(self):
        print("Type in the path and filename of the parser settings.")
        print("Note: .cfg path is appended to the end of the file automatically. Do not specify the file extension.")
        user_input = str(input(">"))
        try:
            self.parser_setting.read(user_input + ".cfg")
        except FileNotFoundError:
            print("Error: File does not exist!")
        except OSError:
            print("Error: Invalid filename!")

    def save_current_parser_settings(self):
        print("Type in the path and filename to save the current parser settings.")
        print("Press Enter without typing any filename to save to default settings.")
        print("Note: .cfg path is appended to the end of the file automatically. Do not specify the file extension.")
        user_input = str(input(">"))
        if user_input == "":
            self.generate_new_default_setting()
        else:
            try:
                self.parser_setting.write(user_input + ".cfg")
            except FileNotFoundError:
                print("Error: File does not exist!")
            except OSError:
                print("Error: Invalid filename!")

    def new_parser_operation(self):
        print("(1) Read one log")
        print("(2) Read multiple slow logs in a folder")
        user_input = str(input(">"))

        # Read one log
        if user_input.lower().strip() == 'l':
            print("Enter file name of log file.")
            user_input = str(input(">"))
            self.load_file(user_input)  # TODO try catch
        # Read multiple logs in a folder
        elif user_input.lower().strip() == '2':
            print("Enter path of log files.")
            user_input = str(input(">"))
            self.load_files(user_input)  # TODO try catch

    def load_file(self, filename):
        pass

    def load_files(self, folder):
        pass

    def generate_new_default_setting(self):
        self.parser_setting.write("cfg/default_setting.cfg")
