#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      maximilian
#
# Created:     09/01/2012
# Copyright:   (c) maximilian 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
from struct import unpack
import odict


class ParentHeader:
    """ parent header """
    def __init__(self):
       self.data = odict.odict() # 順序付きディクショナリクラス

    def __str__(self):
       for k, v in self.data.iteritems():
           print k, v
       return ""

class BitmapParser:

    class FileHeader(ParentHeader):
        """ Bitmap file header """
        def __init__(self):
            ParentHeader.__init__(self)
            self.data[ "type" ]         = "" # ファイルタイプ
            self.data[ "size" ]         = 0  # ファイルサイズ
            self.data[ "reserved1" ]    = 0  # 予約領域1
            self.data[ "reserved2" ]    = 0  # 予約領域2
            self.data[ "offset" ]       = 0  # ファイル先頭から画像データまでのオフセットバイト
    class InfoHeader(ParentHeader):
        """ Bitmap information header """
        def __init__(self):
            ParentHeader.__init__(self)
            self.data[ "size" ]         = 0     # 情報ヘッダサイズ
            self.data[ "width" ]        = 0     # 画像の横幅
            self.data[ "height" ]       = 0     # 画像の縦幅
            self.data[ "plane" ]        = 0     # プレーン数
            self.data[ "bitCount" ]     = 0     # 色ビット数
            self.data[ "compression" ]  = 0     # 圧縮形式
            self.data[ "sizeImage" ]    = 0     # 画像データサイズ
            self.data[ "xPixPerMeter" ] = 0     # 水平解像度
            self.data[ "yPixPerMeter" ] = 0     # 垂直解像度
            self.data[ "cluUsed" ]      = 0     # 格納パレット数[使用色数]
            self.data[ "cluImportant" ] = 0     # 重要色数
    class GraphicData:
        def __init__(self):
            self.data = list()
        def __str__(self):
            return str(self.data)

    def __init__(self):
        self.fh = self.FileHeader()
        self.ih = self.InfoHeader()
        self.g = self.GraphicData()
        self.isLoadFinished = False

    def load(self, path):
        with open(path, 'rb') as f:
            # loading file header
            fhData = unpack("<2sL2HL", f.read(14))
            for i, k in enumerate( self.fh.data.keys() ):
                self.fh.data[ k ] = fhData[ i ]
            #print self.fh
            # loading infomation header
            ihData = unpack("<3L2H6L", f.read(40))
            for i, k in enumerate( self.ih.data.keys() ):
                self.ih.data[ k ] = ihData[ i ]
            #print self.ih
            # loading pixel data
            # ピクセルデータは左下から右上に格納されている
            # alignmentされた行の総ビット数
            lineBit, padding= self.alignment(self.ih.data["width"], self.ih.data["bitCount"])
            # バイナリ読み込みフォーマット
            lineStr = "<" + str(lineBit) + "B"
            # バイナリ読み込みサイズ
            readSize = lineBit
            pixelDataSize = self.ih.data["bitCount"] / 8 # 色値バイト数
            for y in range(0, self.ih.data["height"]):
                self.g.data.insert(0, list())
                value = unpack( lineStr, f.read(readSize) )
                if padding:
                    lineBit -= pixelDataSize
                for x, idx in enumerate( range(0, lineBit, pixelDataSize ) ):
                    self.g.data[0].append( value[ idx ] | value[ idx+1 ] << 8 | value[ idx+2 ] << 16 )
            self.isLoadFinished = True
    def alignment(self, width, bitcount):
        """ alignment 4byte """
        line = (width * bitcount) / 8
        padding = line % 4
        if padding != 0:
            line = ((line / 4) + 1) * 4
        return line, padding

if __name__ == '__main__':
    pass
    #test = BitmapParser('./data/test.bmp')
