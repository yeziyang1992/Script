#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 12:04
# @Author  : linkai
# @File    : config_keyWords_info.py
# @Description :具体表对应关键字段及取值

# todo 修改
keywords = ["user_name", "user_group", "strsrc_ip", "strdst_ip", "app_type_alias", "net_action", "uparea_id",
            "app_name_alias", "app_type_alias", "app_name", "app_type", "src_ip_country", "behavior_num",
            "src_country_hash", "dst_country_hash", "auth_type", "auth_account","attach_md5_hash","protocol","flow",
            'capture_month','insert_month','capture_week','insert_week','src_ip_longitude','src_ip_latitude',
            'dst_ip_longitude','dst_ip_latitude','longitude','latitude','src_ip_country','dst_ip_country',
            'main_account','virtual_account','domain','net_action','data_type','hardware_type','hardware_sign','virtual_account_type','target_account']

# user_name = ['024302031', '121.76.248.255', 'Twitter[Browse]Youtube$encryption/Browsing', 'whitelistuser201',
#              'WLUser-134', 'BLUser-',
#              '61.234.66.198', '432302031', '124302056', '124672056', '568902056', '879852056', '547841056',
#              '789432745', '4784547952']

user_name = ['','20.20.20.20','2001:0DB8:ABCD:EF01:2345:6789:abcd:ef01','whitelistuser001','WLUser-.001',
            'BLUser-.001','nma21205231','902455','Twitter[Browse]Youtube$encryption/Browsing','中文用户名',
            '123456789012345678901234567890123456789012345678901234567890abcdefg','hijklmnopqrstuvwxyz',None,
            '20.WLUser-.','WHitelistUSer002','001BLUser-.','whitelistuser.20.20.20']

# user_name = ['20.20.20.20','','2001:0DB8:ABCD:EF01:2345:6789:abcd:ef01','whitelistuser001','WLUser-.001']

user_group = ['/default/', '/bypass/', '/Chictalk/', '/TestGroup/', '/group1/', '/test/']

app_type = ['IM', 'P2P', 'IoT']

app_name = ['Game_For_Peace', 'Google Data', 'Google Maps', 'Youtube encryption Browsing', 'Facebook[Browse]', 'NETBIOS']

# strsrc_ip = ['121.76.248.255', '61.234.66.198', '36.63.222.240', '139.202.43.58', '36.63.14.190']

strsrc_ip = ['20.20.20.20', '2001:0DB8:ABCD:EF01:2345:6789:abcd:ef01', '192.168.6.119','121.76.248.255', '61.234.66.198', '36.63.222.240', '139.202.43.58', '36.63.14.190']

strdst_ip = ['20.20.20.20', '2001:0DB8:ABCD:EF01:2345:6789:abcd:ef01', '192.168.6.119','121.76.248.255', '61.234.66.198', '36.63.222.240', '139.202.43.58', '36.63.14.190']

# net_action = ['1020120', '1020220', '1020122', '1020123']
# net_action = ['1020120', '1020220', '1020122']
# net_action = ['120121', '120221', '120321']
net_action = [
"120120","20120",
"120220","20220",
"120320","20320",
"120420","20420",
"120520","20520"]

uparea_id = [210213, 220214, 230215,210216, 220217, 230218,210219, 220220, 230221,210222, 220223, 230224]

app_type_json = {'IM': ['Google Data', 'Google Maps', 'Facebook[Browse]', 'BT', 'Game_For_Peace'],
                 'IoT': ['NETBIOS', 'Mijia', 'Youtube encryption Browsing', 'OCSP', 'Youtube Video Upload'],
                 'P2P': ['Twitter[Browse]', 'NTP', 'xiaomi shop', 'Encrypted Youtube Video', 'ODDC'],
                 'Game': ['game_name_1', 'game_name_2', 'game_name_3', 'game_name_4', 'game_name_5'],
                 'Custom_IMO': ['IMO_name_1', 'IMO_name_2', 'IMO_name_3', 'IMO_name_4', 'IMO_name_5']
                 }

app_name_alias = ["APPlntest2", "APPlntest3", "ssl"]
app_type_alias = ["net protocol", "auth_apptype"]
behavior_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
src_ip_country=['Algeria','China','United Kingdom','France','Hong Kong, China','Taiwan, China','Macao, China','阿尔及利亚','中国',
'英国','法国','中国香港','中国台湾','中国澳门','Algeria','Algeria','Algérie','Chine','Royaume-Uni','France','Hong Kong, Chine','Taïwan, Chine',
'Macao, Chine','Algeria','Algeria']

dst_ip_country=['Algeria','China','United Kingdom','France','Hong Kong, China','Taiwan, China','Macao, China','阿尔及利亚','中国',
'英国','法国','中国香港','中国台湾','中国澳门','Algeria','Algeria','Algérie','Chine','Royaume-Uni','France','Hong Kong, Chine','Taïwan, Chine',
'Macao, Chine','Algeria','Algeria']
# src_ip_country = ["Algérie", "Angola", "Bénin", "Botswana", "Burkina Faso", "Burundi", "Cameroun", "Cap-Vert"]
# dst_ip_country = ["Bénin", "Angola", "Burkina Faso", "Burundi", "Cameroun", "Cap-Vert"]

# # 取src_ip_country的hash值
# src_country_hash = [hash(country) for country in src_ip_country]
# # 取dst_ip_country的hash值
# dst_country_hash = [hash(country) for country in dst_ip_country]


dst_country_hash = [21098675,210987654,78904345,43609876,46109876,43109875,
                    43610985,43610985,43610987,43610798,436109872,43610978]

src_country_hash = [210986765,210986765,789042345,436109876,436109876,4361098756,
                    4361098576,4361098576,4361098766,4361079876,4361098726,4361097876]



auth_type = [1020001, 1029999, 1029997]

protocol = [1020001, 1029999, 1029997]

flow = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# auth_account = ['024302031', 'fosln22@promarmed.fr', 'xxjradius122']


# auth_account = ['20.20.20.20', '00:1A:2B:3C:4D:5E', '2001:0db8:85a3:0000:0000:8a2e:0370:7334','::1']

# auth_account = ['nma21205231', 'Twitter[Browse]Youtube$encryption/Browsing', '中文用户名','']


# main_account = ['0573698164@davismooreparts.com', '0601088097@backinbalancegso.com', '13018062221@163.com','22aasnieres@wanadoo.fr',
#                 '554970944579368@groups.facebook.com','a.alenda@djamaa-el-djazair.com','a.bouaoud@amana-tech.com','a.lebeidi@andersonlogistique.com',
#                 'a.purnomoaji@ips.co.id','a308@z3.com']

domain = ['0573698164@davismooreparts.com', '0601088097@backinbalancegso.com', '13018062221@163.com','22aasnieres@wanadoo.fr',
                '554970944579368@groups.facebook.com','a.alenda@djamaa-el-djazair.com','a.bouaoud@amana-tech.com','a.lebeidi@andersonlogistique.com',
                'a.purnomoaji@ips.co.id','a308@z3.com']



virtual_account = ['0573698164@davismooreparts.com',
'0601088097@backinbalancegso.com',
'13018062221@163.com',
'22aasnieres@wanadoo.fr',
'554970944579368@groups.facebook.com',
'a.alenda@djamaa-el-djazair.com',
'a.bouaoud@amana-tech.com',
'a.lebeidi@andersonlogistique.com',
'a.purnomoaji@ips.co.id',
'a308@z3.com','']


virtual_account_type =['davismooreparts.com','backinbalancegso.com','163.com','wanadoo.fr','groups.facebook.com','djamaa-el-djazair.com']

target_account = ['0573698164@davismooreparts.com',
'0601088097@backinbalancegso.com',
'13018062221@163.com',
'22aasnieres@wanadoo.fr',
'554970944579368@groups.facebook.com',
'a.alenda@djamaa-el-djazair.com',
'a.bouaoud@amana-tech.com',
'a.lebeidi@andersonlogistique.com',
'a.purnomoaji@ips.co.id',
'a308@z3.com','']

auth_account = ['0573698164@davismooreparts.com',
'0601088097@backinbalancegso.com',
'13018062221@163.com',
'22aasnieres@wanadoo.fr',
'554970944579368@groups.facebook.com',
'a.alenda@djamaa-el-djazair.com',
'a.bouaoud@amana-tech.com',
'a.lebeidi@andersonlogistique.com',
'a.purnomoaji@ips.co.id',
'a308@z3.com','']

main_account = ['0573698164@davismooreparts.com',
'0601088097@backinbalancegso.com',
'13018062221@163.com',
'22aasnieres@wanadoo.fr',
'554970944579368@groups.facebook.com',
'a.alenda@djamaa-el-djazair.com',
'a.bouaoud@amana-tech.com',
'a.lebeidi@andersonlogistique.com',
'a.purnomoaji@ips.co.id',
'a308@z3.com']

target_account = ['0573698164@davismooreparts.com',
'0601088097@backinbalancegso.com',
'13018062221@163.com',
'22aasnieres@wanadoo.fr',
'554970944579368@groups.facebook.com',
'a.alenda@djamaa-el-djazair.com',
'a.bouaoud@amana-tech.com',
'a.lebeidi@andersonlogistique.com',
'a.purnomoaji@ips.co.id',
'a308@z3.com']

# attach_md5_hash = ['d41d8cd98f00b204e9800998ecf8427e','6dcd4ce23d88e2ee9568ba546c007c84','a93d485c34578a59d3b746af10b1b72b']

# attach_md5_hash = ['2749cc379a697a22016cebf886f71866','f1b115635fec6c9f9a1b89d9f5718dcc','003310eae4f83adb628eeffc73dc45ca','5496b074f9b6d5e347d3eae0c3f183a1','ca338c912042c802affe44b8acb0663c']

attach_md5_hash =[210986765,210986765,789042345,436109875,430987655,410987565,
                    43610985765,43610985765,43610987665,43610798765,43610987265,43610978765]

capture_month = ['2023-11-01','2023-12-01','2024-01-01']

insert_month = ['2023-11-01','2023-12-01','2024-01-01']

src_ip_longitude = ['0.0','180.1','-20.0']

src_ip_latitude = ['0.0','180.1','-20.0']

dst_ip_longitude = ['0.0','180.1','-20.0']

dst_ip_latitude = ['0.0','180.1','-20.0']

longitude = ['0.0','180.1','-20.0']

latitude = ['0.0','180.1','-20.0']

data_type = [1201,1202,1203,1204,1205,201,203,202,204,205,101,102,103,104,105]

hardware_type = ['PC','Mobile','Tablet','Router','Switch','Server','Printer','Camera','Other']
hardware_sign = ['PC','Mobile','Tablet','Router','Switch','Server','Printer','Camera','Other']

# app_name = ['app_name_1','app_name_2','app_name_3','app_name_4','app_name_5','app_name_6','app_name_7','app_name_8','app_name_9','app_name_10']

# app_type = ['1','2','3','4','5','6','7','8','9','10']