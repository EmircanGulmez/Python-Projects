import requests
import json

# URL hatalı olduğu için çalışmaz eğer düzeltilirse sonundaki döviz türü silinecek
api_url = "https://api.exchangeratesapi.io/lates?base="

bozulacakDoviz = input("Bozulacak Döviz Türü: ")
alinacakDoviz = input("Alınacak Döviz Türü: ")
miktar = int(input(f"Ne kadar {bozulacakDoviz} bozdurmak istiyorsunuz: "))

gelen = requests.get(api_url)    # siteden gelen değeri alır
gelen = json.loads(gelen.text)   # siteden alınan değerleri texte alır ve listeye çevirir.


print("1 {0} = {1} {2}".format(bozulacakDoviz, gelen["rates"][alinacakDoviz], alinacakDoviz))
print("{0} {1} = {2} {3}".format(miktar, bozulacakDoviz, miktar * gelen["rates"][alinacakDoviz], alinacakDoviz))


