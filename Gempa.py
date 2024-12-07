class Gempa:
    #konstruktor inisualisasi  atribut lokasi dan skala 
     def __init__(self,lokasi,skala):
  
      #atribut 
        self.lokasi = lokasi 
        self.skala = skala 

     # method menentukan dampak skala gempa
     def dampak(self):
  
         #statement / logika 
         if self.skala < 2:
          print('Dampak dari gempa tidak berasa')
         elif self.skala >=2 and self.skala <=4:
            print('Dampak Gempa bangunan retak-retak')
         elif self.skala >4 and self.skala >= 6:
          print('Dampak bangunan berpotensi roboh')
         elif self.skala > 6: 
           print('Dampak Gempa Berpotensi Tsunami')

            #menampilkan Lokasi dan Skala 
         print(f'Lokasi Gempa:{self.lokasi}')
         print(f'skala gempa {self.skala}')
