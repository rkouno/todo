from .models import Workbook
from commons.const import appconst
from commons.util import utils

def getList():
    # 空フォルダの削除
    utils.folderDelete(appconst.FOLDER_TORRENT)
    file_folder = []
    # 書籍ファイルの取得
    for book in utils.getFiles(appconst.FOLDER_TORRENT, appconst.EXTENTION_BOOK):
        file_folder.append(book)
    # 書籍フォルダの取得
    # for folder in utils.getFolders(appconst.FOLDER_TORRENT):
    #     file_folder.append(folder)
    
    Workbook.objects.all().delete()

    for item in file_folder:
        name = utils.getFileName(item)
        # 登録
        Workbook.objects.create(
            process='',
            path = item,
            name = name,
            genrue_id = '',
            genrue_name = '',
            author_id = '',
            story_by = '',
            art_by = '',
            book_id = '',
            title = '',
            sub_title = '',
            volume = 0,
            book_name = '',
            save_path = '',
            exist_flg = False,
        )
