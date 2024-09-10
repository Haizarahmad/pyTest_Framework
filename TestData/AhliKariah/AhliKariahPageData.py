import openpyxl


class AhliKariahPageData:

    @staticmethod
    def getData(PATH):
        Dict = []
        book = openpyxl.load_workbook(PATH)
        sheet = book.active

        data = {}
        for j in range(3, sheet.max_row + 1):
            if sheet.cell(row=j, column=5).value is not None:
                data[sheet.cell(row=j, column=5).value] = str(sheet.cell(row=j, column=6).value)
        Dict.append(data)

        return Dict

