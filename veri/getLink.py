import requests
from bs4 import BeautifulSoup
rows = []
columns = ['listing title', 'listing url', 'listing image url', 'location', 'Project type', 'Status', 'Size']

toplamUrun = 0
for sayfaNo in range(1,3):
     url = "https://www.n11.com/telefon-ve-aksesuarlari/cep-telefonu?pg=" + str(sayfaNo)
     r = requests.get(url)
     soup = BeautifulSoup(r.content,"lxml")
     urunler =soup.find_all("li",attrs={"class":"column"})
# /* satır sutun*/print-urun ekrana basma
# /* urunlerrin baslığını alma*/print-urun ekrana basma
   for urun in urunler:
        urunAdi  = urun.a.get("title")
        urunLink = urun.a.get("href")
        print(urunAdi)
    # /* urun içine gir belirttiklerimi al*/alamazsan bulunamadı yaz
        try:
           urun_r = requests.get(urunLink)
           toplamUrun =+ 1
        except Exception:
           print("ürün bilgisi alınamadı")
    # /* urun içine gir belirttiklerimi al*/
        urun_soup  = BeautifulSoup(urun_r.content,"lxml")
        ozellikler = urun_soup.find_all("div",attrs={"class":"feaItem"})
    for ozellik in ozellikler:
        urun_label = (ozellik.find("span",attrs={"class":"label"}).text
        try:
           urun_data = (ozellik.find("span",attrs={"class":"data"}).text)
        except Exception:
        # /* urun içine gir a içinden datayı bul onun içindeki spana gir ve bana nokta textini ver*/
           urun_data = (ozellik.find("a",attrs={"class":"data"}).find("span").text
           print("{} : {}".format(urun_Label, urun_data))  
    print("#"*10)
# /* excele bas*/print-urun ekrana basma

row = [listing_title, listing_url, listing_image_url, property_location, property_type, property_status, property_size]  
rows.append(row)

df = BeautifulSoup.DataFrame(rows, columns=columns)
df.to_excel('n11 cep telefonu.xlsx', index=False)
print('File Saved')

print("Toplam {} ürün bulundu".format(ToplamUrun))
