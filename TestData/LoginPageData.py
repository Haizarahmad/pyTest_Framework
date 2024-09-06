# import openpyxl
class LoginPageData:

    test_LoginPage_valid_data = [
        {"username": "admin", "password": "123", "ExpectedResult": "You have been successfully log in"},
        {"username": "admin2", "password": "123", "ExpectedResult": "You have been successfully log in"}
    ]

    test_LoginPage_invalid_data = [
        {"username": "amin", "password": "13", "ExpectedResult": "No user have been register into the system"}
    ]

    test_admin_data = [
        {"username": "admin", "password": "123"}
    ]

    # @staticmethod
    # def getTestData():
    #     Dict = {}
    #     book = openpyxl.load_workbook("C:\\Users\\User\\PycharmProjects\\Pytest_Framework\\TestData\\testdata_login.xlsx")
    #     sheet = book.active
    #     for i in range(1, sheet.max_column + 1):
    #         if sheet.cell(row=1, column=i).value == "InputData":
    #
    #             for j in range(3, sheet.max_row + 1):
    #                 if sheet.cell(row=j, column=i) is not None:
    #                     Dict["username"] = sheet.cell(row=j, column=i)


