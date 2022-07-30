# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(csv_save_path,qualifying_loans):
    """Create and write the CSV file to path provided.

    Args:
        csv_save_path (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the filtered qualifying loans.

    """
    # @TODO: Complete the usability dialog for savings the CSV Files.

    
    #Open the file in write mode
    with open(csv_save_path,"w",newline="") as csvfile:

        #create a writer
        csvwriter = csv.writer(csvfile)

        #write back the header
        output_file_header=["Lender","Max Loan Amount","Max LTV","Max DTI","Min Credit Score","Interest Rate"]
        
        csvwriter.writerow(output_file_header)

        #write the qualifying loans
        csvwriter.writerows(qualifying_loans)