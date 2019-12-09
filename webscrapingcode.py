# Herkese merhabalar. Bu web scraping ile takipçi sayısını yaml dosyasına kaydetme uygulaması yaptım.
# https://github.com/YuceMantar buradan projenin orjinal haline ulaşabilirsiniz.
# Bana mhmtlorhan@gmail.com ile ulaşabilirsiniz. Umarım işinize yarar! Kolay gelsin

import requests,sys,time,threading
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, QtGui
uygulama= QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()
window.setWindowTitle("Web Scraping")
window.setGeometry(100, 100, 500, 500)

window.setMinimumHeight(500)
window.setMinimumWidth(500)

window.setMaximumHeight(500)
window.setMaximumWidth(500)

window.setWindowIcon(QtGui.QIcon("icon.ico"))
def dongu():
    while True:
        main = requests.get("https://twitter.com/temhemnahroo")
        firstexamp = requests.get("https://twitter.com/ThePSF")
        secondexamp = requests.get("https://twitter.com/Twitter")
        thirdexamp = requests.get("https://twitter.com/instagram")
        fourthexamp = requests.get("https://twitter.com/facebook")

        soup = BeautifulSoup(main.content,"html5lib")
        soup2 = BeautifulSoup(firstexamp.content,"html5lib")
        soup3 = BeautifulSoup(secondexamp.content,"html5lib")
        soup4 = BeautifulSoup(thirdexamp.content,"html5lib")
        soup5 = BeautifulSoup(fourthexamp.content,"html5lib")

        main1=soup.find('a',{'class':'ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor','data-nav':'followers'})
        main2=main1.find('span',{'class':'ProfileNav-value'}).get_text()

        firstexamp1=soup2.find('a',{'class':'ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor','data-nav':'followers'})
        firstexamp2=firstexamp1.find('span',{'class':'ProfileNav-value'}).get_text()

        secondexamp1=soup3.find('a',{'class':'ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor','data-nav':'followers'})
        secondexamp2=secondexamp1.find('span',{'class':'ProfileNav-value'}).get_text()

        thirdexamp1=soup4.find('a',{'class':'ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor','data-nav':'followers'})
        thirdexamp2=thirdexamp1.find('span',{'class':'ProfileNav-value'}).get_text()

        fourthexamp1=soup5.find('a',{'class':'ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor','data-nav':'followers'})
        fourthexamp2=fourthexamp1.find('span',{'class':'ProfileNav-value'}).get_text()

        with open("C:/Users/mhmtl/OneDrive/Masaüstü/mntr_apps/database.yml", "a") as f:
            f.write("main\t  ")

        dosya = open("database.yml", "w")


        etiket1.setText("Şahsi Takipçi:"+str(main2))
        etiket2.setText("Python Takipçi:"+str(firstexamp2))
        etiket3.setText("Twitter Takipçi:"+str(secondexamp2))
        etiket4.setText("İnstagram Takipçi:"+str(thirdexamp2))
        etiket5.setText("Facebook Takipçi:"+str(fourthexamp2))

        dosya.write("- Brand: main \n Followers:"+str(main2))
        dosya.write("\n- Brand: firstexamp \n Followers:"+str(firstexamp2))
        dosya.write("\n- Brand: secondexamp \n Followers:"+str(secondexamp2))
        dosya.write("\n- Brand: thirdexamp \n Followers:"+str(thirdexamp2))
        dosya.write("\n- Brand: fourthexamp \n Followers:"+str(fourthexamp2))

        dosya.close()
        time.sleep(5)

is_parcasi = threading.Thread(target=dongu)
is_parcasi.start()

etiket1 = QtWidgets.QLabel(window)
etiket1.setText("                                                ")
etiket1.move(30, 30)

etiket2 = QtWidgets.QLabel(window)  
etiket2.setText("                                                ")
etiket2.move(30, 90)

etiket3 = QtWidgets.QLabel(window) 
etiket3.setText("                                                ")
etiket3.move(30, 150)

etiket4 = QtWidgets.QLabel(window)
etiket4.setText("                                                ")
etiket4.move(30, 210)

etiket5 = QtWidgets.QLabel(window)
etiket5.setText("                                                ")
etiket5.move(30, 270)


window.show()                         
sys.exit(uygulama.exec_())  
