import pathlib
import unittest
from tempfile import TemporaryDirectory
from unittest.mock import patch
from urllib.error import URLError

THUMBNAIL_URL = (
    "http://books.google.com/books/content"
    "?id=OgtBw76OY5EC&printsec=frontcover"
    "&img=1&zoom=1&edge=curl&source=gbs_api"
)

class SaveThumbnailsTest(unittest.TestCase):
    def setUp(self):
        # 一時ディレクトリを作成する
        self.tmp = TemporaryDirectory()

    def tearDown(self):
        # 一時ディレクトリを片づける
        self.tmp.cleanup()

    def test_save_thumbnails(self):
        from booksearch.core import Book
        book = Book({"id": "", "volumeInfo": {
            "imageLinks": {
                "thumbnail": THUMBNAIL_URL
            }}})

        # 処理を実行し、ファイルが作成されることを確認する
        filename = book.save_thumbnails(self.tmp.name)[0]
        self.assertTrue(pathlib.Path(filename).exists())

    # テスト対象のsave_thumbnails()が利用する参照名を指定
    @patch("booksearch.core.get_data")
    def test_save_thumbnails(self, mock_get_data):
        from booksearch.core import Book

        # 先ほど取得したサムネイル画像データをモックの戻り値にセット
        data_path = pathlib.Path(__file__).with_name("data")
        mock_get_data.return_value = (
            data_path / "y35oDwAAQBAJ_smallThumbnail.jpeg").read_bytes()

        book = Book({"id": "", "volumeInfo": {
            "imageLinks": {
                "thumbnail": THUMBNAIL_URL
            }}})
        filename = book.save_thumbnails(self.tmp.name)[0]

        # get_data()呼び出し時の引数を確認
        mock_get_data.assert_called_with(THUMBNAIL_URL)

        # 保存されたデータを確認
        self.assertEqual(data_path, filename.read_bytes())

class GetBooksTest(unittest.TestCase):
    def test_get_books_no_connection(self):
        from booksearch.core import get_books

        # 一時的にネットワークアクセスを遮断
        with patch("socket.socket.connect") as mock:
            # connect()が呼び出された際に不正な値を返す
            mock.return_value = None
            with self.assertRaisesRegex(URLError, "urlopen error"):
                # 例外が発生する処理をwithブロック内で実行する
                get_books(q="Python")