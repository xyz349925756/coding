#!/usr/bin/python3
# -*-coding:utf-8-*-
# Time    :2022/1/18  21:13
# Author  :xyz34
# Email   :xyz349925756@hotmail.com
# File    :快递分拣1.py
# Project :coding

pos_list = [
	['王*龙', '北京市海淀区苏州街大恒科技大厦南座4层'],
	['庞*飞', '北京市昌平区汇德商厦四楼403'],
	['顾*锐', '江苏省扬州市三垛镇工业集中区扬州市立华畜禽有限公司'],
	['王*飞', '上海市徐汇区上海市徐汇区H88越虹广场B座5E'],
	['华*升', '北京市海淀区杰睿大厦'],
	['朱*锴', '上海市浦东新区川沙新镇华川家园33号楼503'],
	['陈*盼', '浙江省杭州市闲林街道，西溪华东园，十幢一单元401。'],
	['司*鹏', '河南省鹤壁市淇滨大道310号  鹤壁京立医院'],
	['聂*睿', '河北省石家庄市中山路勒泰中心写字楼b座11层'],
	['张*', '辽宁省本溪市明兴丽城九号楼四单元'],
	['冉*晗', '河北省石家庄市体育南大街385号'],
	['高*杰', '北京市朝阳区广渠路42号院3号楼，408'],
	['李*国', '安徽省合肥市新站区淮合花园'],
	['常*源', '江苏省南京市白下路242号，南京市红十字医院，放射科'],
	['张*玉', '河北省沧州市新居然家居广场'],
	['王*川', '上海市奉贤区南桥镇 贝港七区'],
	['冀*庆', '河北省保定市河北大学坤兴园生活区'],
	['胡*晨', '浙江省宁波市浙江省宁波市江东区中山首府A座2004室'],
	['尹*婷', '湖北省武汉市武汉大学信息学部'],
	['李*东', '辽宁省大连市大关一街3号3-3-1'],
	['张*', '天津市河西区隆昌路94号（天津科技馆）'],
	['刘*', '湖北省黄冈市城关镇'],
	['阿*亚', '内蒙古呼和浩特市包头东接民望家园1区3号楼2单元1501'],
	['孙*云', '山东省济南市山东省济南市历下区祥泰汇东国际，一号楼3005室'],
	['曹*亮', '黑龙江省大庆市服务外包产业园D1'],
	['侯*琦', '上海市长宁区金钟路凌空soho16号楼3楼'],
	['郭*峰', '河南省商丘市高新技术开发区恒宇食品厂'],
	['赵*生', '河北省唐山市朝阳道与学院路路口融通大厦2408室'],
	['张*', '陕西省咸阳市文汇东路6号西藏民族大学'],
	['刘*民', '北京市大兴区南海家园四里7号楼1单元902'],
	['郭*兰', '湖北省武汉市湖北省'],
	['张*强', '河北省张家口市经开区钻石南路11号'],
	['鞠*龙', '山东省潍坊市玉清街江山帝景B区12号楼一单元14楼'],
	['李*', '北京市海淀区西二旗智学苑5号楼超市'],
	['许*康', '北京市西城区西单北大街甲133号'],
	['叶*生', '江苏省扬州市扬子江中路756号'],
	['赵*兴', '北京市海淀区西二旗上地信息路1号金远见大楼华纬讯301'],
	['徐*革', '北京市海淀区闵庄路3号102栋二层206'],
	['徐*', '安徽省淮南市金荷小区(金格商场旁)'],
	['雷*', '北京市朝阳区望京街道望京sohoT1C座1201'],
	['庄*', '浙江省杭州市恒生电子大厦'],
	['蔡*恩', '湖北省武汉市仁和路沙湖港湾B区1103'],
	['陈*', '江苏省苏州市巴城镇湖滨北路193号牛吃蟹庄'],
	['黄*', '北京市朝阳区霄云路26号鹏润大厦A座33层'],
	['魏*飞', '河北省石家庄市新石北路与红旗大街交口开元大厦502室'],
	['张*', '山东省济南市兴港路三庆城市主人'],
	['段*琪', '山西省临汾市福利路尧乡小区'],
	['刘*', '北京市昌平区龙禧三街骊龙园601'],
	['王*生', '上海市杨浦区邯郸路复旦大学遗传学楼319室'],
	['王*君', '江苏省扬州市叶挺路318号建行营业部'],
	['王*义', '北京市东城区环球贸易中心D座'],
	['李*', '陕西省汉中市同沟寺镇晨光村二组'],
	['裴*宇', '吉林省四平市岭西新耀豪庭7栋'],
	['丁*', '山东省烟台市大季家镇芦洋村'],
	['刘*铎', '黑龙江省佳木斯市火电小区桥头浴池附近惠惠干洗店'],
	['樊*', '浙江省宁波市文苑风荷201-301'],
	['陈*瑞', '安徽省宣城市安徽省宣城市宣州区薰化路301合肥工业大学宣城校区'],
	['崔*峰', '浙江省台州市福溪街道始丰西路43号501室'],
	['徐*', '湖北省武汉市三金雄楚天地1号楼1210'],
	['王*', '浙江省宁波市浙江工商职业技术学院信息中心'],
	['闫*', '上海市浦东新区蓝天路368弄1号301室'],
	['于*泉', '吉林省四平市金星书苑小区8号楼5单元102室'],
	['刘*萌', '河北省秦皇岛市抚宁镇交通局家属院3-2-201'],
	['石*', '安徽省宣城市薰化路301'],
	['王*雯', '甘肃省兰州市天水南路222号兰州大学'],
	['王*朝', '河南省郑州市嵩山南路政通路升龙城六号院'],
	['金*晶', '吉林省延边州延吉市新兴街民安委11'],
	['蒋*彬', '辽宁省本溪市新城北岸，恒大绿洲'],
	['牛*鑫', '黑龙江省鸡西市南山路康光二号楼中雅发廊'],
	['陈*宏', '山西省太原市太原理工大学'],
	['刘*', '山西省运城市卿头镇'],
	['陈*杰', '浙江省宁波市高新区研发园A5幢7楼多维时空科技有限公司'],
	['郝**', '山东省德州市焦庙镇'],
	['焦*', '山西省长治市太行西街金威超市太西店金威快购办公室'],
	['李*旗', '北京市昌平区沙河镇汇德商厦4楼403老男孩教育'],
	['通*大都', '北京市丰台区万泉寺东路9号院1栋1单1704'],
	['孙*川', '浙江省金华市佛堂镇雅西村双溪口便民超市'],
	['宋*', '安徽省合肥市上派镇滨河家园9栋2102'],
	['李*', '陕西省安康市汉滨区新城街道南环东路口桃园小区大门口'],
	['李*连', '北京市昌平区立汤路北七家威尼斯花园2区2-3'],
	['籍*旭', '北京市房山区良乡鸿顺园西区20号楼3单元601'],
	['韩*嵩', '北京市昌平区立汤路威尼斯花园2区2-3'],
	['曹*', '北京市朝阳区东三环北路28号博瑞大厦B座'],
	['贺*', '上海市徐汇区古美路1515号19号楼1101室'],
	['关*轩', '山西省长治市石哲镇'],
	['罗*', '河北省廊坊市书香苑小区四号楼'],
	['段**', '北京市朝阳区酒仙桥东路M5世纪互联'],
	['杜*伟', '北京市昌平区汇德商厦老男孩教育'],
	['王*', '北京市昌平区汇德商厦四楼'],
	['赵*波', '上海市闵行区上海市闵行区莘庄镇庙泾路水清三村52号32弄402室'],
	['许*', '北京市海淀区西北旺镇中海枫涟山庄北门对面中心'],
	['李*成', '北京市昌平区沙河镇于辛庄村天利合家园'],
	['刘*', '江苏省南京市兴智路6号兴智科技园A栋7层'],
	['张*涛', '安徽省合肥市安徽省合肥市庐阳区寿春路156号古井百花大厦大厦A座2603'],
	['高*', '上海市虹口区欧阳路351弄10号楼104室'],
	['谷*成', '浙江省杭州市城厢街道 下湘湖路1号'],
	['王*玉', '上海市嘉定区南翔镇'],
	['刘*海', '北京市海淀区玉渊潭南路3号水科院万方城科技楼'],
	['杨*娟', '安徽省合肥市清源路中铁国际城和畅园'],
	['谢*桥', '北京市海淀区丰秀中路3号院9号楼北京数码大方科技股份有限公司'],
	['张*', '陕西省咸阳市北上召秦楚汽车城别克雪佛兰4s店'],
	['邵*龙', '北京市海淀区西北旺镇大牛坊社区四期4号楼1单元301'],
	['耿*涛', '北京市朝阳区三间房东柳巷甲一号意菲克大厦A座'],
	['孙*周', '北京市东城区东花市街道便宜坊写字楼10层，恒信通大厦。就在崇文门地铁站口旁边'],
	['于*涵', '山东省济南市舜耕路舜耕山庄宿舍'],
	['陈*', '上海市普陀区近铁城市广场北座15楼'],
	['马*', '北京市昌平区沙河镇松兰堡村西口兴业家园6号楼'],
	['李*宇', '江苏省苏州市工业园区苏雅路158号华盛广场3楼东北证券304室'],
	['王*杰', '河北省邯郸市后仓街39号'],
	['刘*明', '河北省唐山市卫国北路305张家口银行'],
	['王*凡', '天津市南开区卫津路92号天津大学鹏翔公寓'],
	['郭*军', '上海市浦东新区郭守敬路498号浦东软件园16号3楼'],
	['宋*东', '北京市丰台区万寿路南口288号华信大厦'],
	['江*', '安徽省阜阳市临海尚城B区2单元，19号楼'],
	['吴*', '河南省郑州市经三路与东风路交汇处金城国际广场6#东单元2403'],
	['祁*雄', '湖北省武汉市洪山区白沙洲大道武汉科技大学北苑'],
	['吕*', '上海市嘉定区上海市嘉定区嘉罗公路2019号'],
	['黄*', '湖北省武汉市国家光电实验室'],
	['常*旗', '山东省潍坊市林海生态博览园'],
	['陈*', '上海市虹口区吴淞路218号宝矿大厦2501A'],
	['郑*琳', '北京市丰台区西马金润家园2区10号楼11单元11-2-1'],
	['姚*峰', '江苏省无锡市江苏省无锡市滨湖区龙山龚巷213#'],
	['徐*', '浙江省杭州市余杭塘路515矩阵国际中心2号楼705'],
	['沈*', '上海市长宁区金钟路968号凌空SOHO11号楼506室'],
	['王*', '上海市浦东新区川沙路1666弄79号803'],
	['徐*', '山东省日照市安东卫街道汾水村'],
	['路*领', '北京市丰台区四方景园一区3号楼1006室'],
	['张*巍', '河南省开封市西环路北段青年城8号楼3单元302'],
	['王*俊', '江苏省盐城市新都路29号紫金大厦19楼'],
	['姜*波', '北京市朝阳区北京市朝阳区阜通东大街1号望京soho塔三B座17层1707'],
	['曹*翎', '江苏省苏州市科教新城太和丽都31-1604'],
	['齐*', '江苏省南京市天元东路228号莱茵量子国际'],
	['高*', '山西省太原市经济技术开发区龙盛街2号国药控股'],
	['刘*', '北京市海淀区中关村丹棱街中国电子大厦B座1608'],
	['陈*山', '安徽省六安市南港镇'],
	['赵*', '黑龙江省哈尔滨市锦山路5号，黑龙江省地质科学研究所'],
	['伍*', '安徽省芜湖市泉塘镇'],
	['白*潮', '上海市浦东新区康桥镇环桥路2585弄文怡苑一期27号楼301'],
	['黄*曦', '北京市朝阳区西坝河南路3号2层201室 同创双子信息技术股份有限公司'],
	['牟*强', '山东省日照市山东东路619号 广电网络公司'],
	['李*运', '上海市松江区沪亭南路208弄109号801室'],
	['杨*', '北京市朝阳区安苑路20号世纪兴源大厦304'],
	['宋*伟', '河北省石家庄市高头乡西高村'],
	['任*鹏', '陕西省西安市锦业一路29号 龙旗科技园 6层 西安和利时系统工程有限公司'],
	['孙*洲', '北京市东城区东花市街道便宜坊写字楼10层，恒信通公司。就在崇文门地铁站旁边'],
	['张*义', '上海市浦东新区三舒路181弄2号904'],
	['门*意', '黑龙江省哈尔滨市文昌街238号联通系统集成有限公司'],
	['陈*维', '上海市虹口区欧阳路196号26栋2楼'],
	['周*涛', '浙江省嘉兴市施家北路陈家浜1号'],
	['吴*', '江苏省苏州市工业园区星湖街328号11栋'],
	['苏*', '河南省郑州市登封路晨光社区14号院绿田野超市'],
	['王*', '陕西省西安市雁塔区雁翔路58号西安理工大学曲江校区'],
	['赵*龙', '河北省廊坊市燕郊经济开发区福成大酒店东福成行政中心三楼信息部'],
	['范*勇', '江苏省苏州市苏州市吴中区木渎镇胥口镇621号斯莱克精密设备股份有限公司'],
	['白*', '北京市东城区安定门外大街10号楼415'],
	['刘*', '北京市昌平区回龙观镇二拨子新村东区7号楼1单元402'],
	['钱*庭', '江苏省江苏省泰州市姜堰区南苑新村58号'],
	['王*', '北京市朝阳区北京市朝阳区摩托罗拉大厦'],
	['杨*', '北京市朝阳区阜荣街10号首开广场5楼'],
	['姬*飞', '北京市昌平区宏福创业园15号创昱'],
	['熊*威', '浙江省杭州市万塘路252号计量大厦10楼'],
	['薛*', '山东省济南市高新区新泺大街888号福瑞达'],
	['贾*凯', '上海市浦东新区鹤永路751弄汇贤雅苑'],
	['孟*震', '上海市宝山区淞南镇祥腾生活广场，8栋816室'],
	['刘*', '河南省洛阳市城关镇人民路21号'],
	['杨*凯', '湖北省武汉市中国地质大学北区1栋'],
	['王*', '上海市浦东新区环桥路1137弄秀怡苑31号楼302'],
	['夏*', '北京市朝阳区垂杨柳东里11号楼3单元402'],
	['张*宇', '北京市海淀区中关村南大街6号中电信息大厦1207'],
	['蔡*', '陕西省西安市凤城八路天朗御湖一号楼二单元（西门）'],
	['高*', '新疆乌鲁木齐市民主路99号建行大厦12楼审计室'],
	['孙*园', '陕西省西安市丈八沟街道科技五路8号数字大厦'],
	['王*亚', '北京市朝阳区华盛乐章b座1708'],
	['李*博', '山东省淄博市索镇花园小区5#2单元202室'],
	['方*', '北京市海淀区北洼西里33号清华同方研究院'],
	['杨*东', '上海市闵行区梅陇镇高兴路高兴花园一街坊14号501'],
	['袁*', '陕西省西安市高新四路南窑头东区22排11号'],
	['王*', '天津市河北区建国道地铁站B口旁青创中心'],
	['程*磊', '北京市西城区北三环中路27号商房大厦5楼'],
	['陈*琦', '安徽省合肥市徽州大道与九华山路交叉口信旺九华国际2419'],
	['刘*杰', '北京市大兴区亦庄经济开发区地盛北街1号35号楼2栋北京如风达快递有限公司'],
	['侯*森', '北京市朝阳区北苑路潮驿178'],
	['胡*辉', '浙江省杭州市瑞立东方花城2-2-503'],
	['杨*平', '北京市昌平区沙河镇于辛庄村赋腾公寓'],
	['黄*', '浙江省杭州市衢江路耀江福村3单元602'],
	['李*', '上海市黄浦区黄浦区北京东路288弄66号甲，后门201室'],
	['邹*', '安徽省淮北市南坪镇黄沟村邹圩庄'],
	['刘*', '北京市昌平区沙河镇赋腾公寓E516'],
	['彭*', '北京市望京SOHOt3  40层'],
	['张*乾', '河南省周口市八一路人民路交叉口医药局家属楼'],
	['贺*梦', '北京市通州区永顺镇世纪星城92号楼二单元'],
	['冯*琴', '北京市海淀区金澳国际写字楼1115  中汇'],
	['邓*亮', '湖北省武汉市云林街台北一路58号'],
	['李*沙', '北京市昌平区城南街道北清路珠江摩尔国际大厦五号楼二单元906'],
	['徐*瑞', '上海市徐汇区古美路1595号宝石园27号楼2楼D区'],
	['梁*', '陕西省西安市电子二路18号(西安石油大学)'],
	['徐*', '浙江省衢州市西区广电大楼'],
	['雷*强', '河南省信阳市汪桥镇街道滨河花园A幢6208'],
	['张*亮', '天津市河西区郁江道17号陈塘科技328'],
	['陈*', '上海市浦东新区东方路1217号陆家嘴金融服务广场15楼'],
	['郭*', '北京市昌平区北七家镇东三旗365号'],
	['李*扬', '上海市浦东新区北蔡镇北艾路1500弄6号楼203'],
	['汝*明', '吉林省长春市长春光机所研究生部D栋'],
	['朱*懿', '上海市静安区陕西北路66号科恩国际中心1027室'],
	['刘*', '上海市浦东新区五莲路 锦河苑'],
	['任*荣', '陕西省西安市软件新城软件公寓'],
	['王*', '上海市闵行区莲花路2080弄50号C幢3楼'],
	['崔*斌', '北京市房山区阎村镇焦庄村四里'],
	['王*强', '浙江省杭州市物联网街451号芯图大厦17楼'],
	['姬*玲', '黑龙江省哈尔滨市长江路462号悦山国际c座1单元2501'],
	['T*m', '上海市浦东新区浦东大道3040弄丽江锦庭1号楼'],
	['李*宇', '黑龙江省绥化市十道街升平小区15号楼1单元102室'],
	['董*', '河南省郑州市崇高路与嵩山路交叉口北黄河商务酒店'],
	['杨*辉', '江苏省镇江市江苏大学F 区'],
	['韩*鉴', '北京市门头沟区滨河路葡东小区七号楼4层D门'],
	['罗*若', '陕西省西安市龙首北路宫园一号5号楼4单元'],
	['王*', '北京市海淀区上地东路盈创动力大厦e座801c源清慧虹信息科技'],
	['马*', '湖北省武汉市庙山中路10号名湖豪庭7栋1403'],
	['常*峰', '山西省太原市迎新街'],
	['侯*', '浙江省杭州市江陵路1541号'],
	['许*娟', '上海市宝山区殷高西路高境二村177号502'],
	['徐*飞', '湖北省武汉市潘塘街喻大村梅家大湾'],
	['崔*腾', '辽宁省沈阳市虹桥路15号富雅豪临'],
	['张*俊', '新疆巴音郭楞州石化大道塔指1区25栋403'],
	['严*', '北京市大兴区清源北路16号，校长大厦'],
	['李*', '北京市大兴区十八里店乡横街子村64号柠檬家园B113'],
	['于*佳', '北京市朝阳区郎园2号A座2层'],
	['张*江', '北京市海淀区海淀区上地三街9号金隅嘉华大厦Ｆ座703室'],
	['萌*', '北京市西城区金融街邮政集团公司'],
	['张*宾', '河南省郑州市文治路泰祥投资集团楼下新锐广告'],
	['彭*灿', '江苏省苏州市玉山镇印象欧洲17#606'],
	['王*亮', '北京市朝阳区双营路11号美立方4号楼4单元602'],
	['朱*伦', '北京市海淀区西三环中路19号海军大院西门顺丰快递'],
	['杜*', '河北省石家庄市河北科技大学新校区26号'],
	['董*', '北京市朝阳区雅宝路华声国际大厦'],
	['朱*', '江苏省镇江市延陵镇'],
	['段*', '山东省临沂市银雀山街道万阅城A座1207'],
	['朱*', '北京市昌平区北京联合大学昌平校区'],
	['陈*章', '北京市昌平区沙河镇白沙路汇德商厦老男孩教育'],
	['肖*雅', '北京市昌平区沙河汇德商厦4楼老男孩儿教育'],
	['赵*明', '北京市昌平区沙河顺沙路汇德商厦老男孩教育403'],
	['邹*', '宁夏银川市上海路福州街口云峰盛大药房'],
	['袁*', '辽宁省锦州市辽宁省凌海市国庆路33B号2单元23室'],
	['陈*', '浙江省杭州市昌化电站里56号骏程瓷砖店'],
	['索*辉', '辽宁省沈阳市浑南区创新路117号东软医疗系统有限公司'],
	['李*', '北京市大兴区天宫院地铁站熙悦春天小区'],
	['张*', '陕西省西安市电子城街道高新领域4号楼'],
	['王*', '山西省吕梁市一家庄小区三期五号楼'],
	['钟*', '陕西省商洛市商洛学院'],
	['薛*', '江苏省泰州市口岸街道向阳北路94号农商行'],
	['张*强', '甘肃省兰州市北滨河西路666号（中国移动甘肃分公司）'],
	['姚*飞', '上海市浦东新区成山路1728弄88号'],
	['赵*宁', '浙江省金华市光南路898号金华移动公司'],
	['张*昌', '北京市昌平区回龙观东大街 矩阵小区 11楼1单元1102室'],
	['董*亨', '上海市嘉定区曹安公路4800号同济大学嘉定校区'],
	['李*根', '北京市昌平区马连店4号楼2单元'],
	['贾*新', '北京市海淀区学院路29号'],
	['吕*', '浙江省舟山市高亭镇军民路106号'],
	['张*东', '河南省周口市西华县基城高中'],
	['李*东', '河北省石家庄市新石中路，物联网大厦10层'],
	['韩*泰', '山东省青岛市青岛农业大学西苑'],
	['邵*遥', '浙江省杭州市塘栖镇张家墩路65号博乐展具内'],
	['李*泽', '河南省郑州市郑东新区龙子湖高校园区郑州信息科技职业学院'],
	['沈*蕾', '浙江省杭州市下沙学源街中国计量大学'],
	['冯*明', '上海市浦东新区张江路华夏中路 虹御公寓'],
	['海*', '浙江省杭州市良渚街道大陆村邱家桥桥南3号'],
	['刘*龙', '北京市通州区台湖镇次渠嘉园8区1号楼1705号'],
	['王*宇', '河南省安阳市红旗路天宇国际三号楼四单元'],
	['宋*波', '北京市海淀区龙翔路甲1号泰翔商务楼508'],
	['周*萧', '北京市昌平区回龙观镇史各庄村176号'],
	['梁*升', '吉林省吉林市承德街45号吉林化工学院'],
	['陈*龙', '上海市浦东新区郭守敬路498号23号楼23215'],
	['张*', '上海市徐汇区桂林路402号 诚达创意园76幢407室 银基科技'],
	['何*畅', '河南省周口市西华县箕城高中'],
	['欧*', '北京市丰台区东营里5号院8号楼2单元401'],
	['张*', '陕西省西安市陕西西安思源学院'],
	['曹*', '浙江省宁波市白沙街道新马路61弄江北区农林水利局'],
	['陈*刚', '宁夏银川市上海东路银佐家园东区11-1-501'],
	['喻*明', '湖北省武汉市徐东'],
	['陈*余', '北京市海淀区甘家口街道阜成路北二街阜光里小区7号楼二单元102'],
	['刘*博', '山西省太原市小店区平阳路42号山西省自动化研究所'],
	['王*', '北京市大兴区亦庄经济技术开发区大族广场T5，6层洪泰空间c033'],
	['褚*文', '湖北省武汉市明伦正街明伦生鲜市场9号'],
	['乔**', '河北省衡水市香榭丽都2号楼1单元 2603'],
	['貟*杰', '上海市宝山区上海市宝山区陆翔路678弄62号903'],
	['甘*德', '北京市海淀区四季青杏石口路甲18号航天信息园'],
	['杨*奖', '北京市东城区东单北大街1号国旅大厦502'],
	['李*', '北京市海淀区北京市海淀区中关村南大街9号理工科技大厦207'],
	['刘*', '浙江省杭州市紫荆花路金月巷嘉禾花苑'],
	['刘*亮', '北京市朝阳门'],
	['聂*敏', '上海市浦东新区高博路188弄1号楼1903室'],
	['刘*正', '山东省青岛市流亭街道洼里社区八号楼尚美美发'],
	['杨*强', '陕西省西安市枣园路万科金色悦城'],
	['聂*', '湖北省武汉市台银大厦1单位1楼'],
	['刘*', '上海市闵行区闵驰一路29弄3号1101'],
	['郭*', '青海省西宁市互助东路12号海亮大都汇'],
	['芦*坤', '北京市朝阳区北京工人体育场3号看台2号楼1706'],
	['晋*林', '上海市杨浦区隆昌路619号城市概念10号b座'],
	['董*', '浙江省杭州市丰潭路城西银泰E2幢10楼'],
	['刘*', '湖北省武汉市中国地质大学（北区）'],
	['马*', '河北省保定市保定市南市区朝阳南大街哈弗技术中心2076号包裹站'],
	['王*超', '黑龙江省哈尔滨市永泰城3号楼1单位1304'],
	['孙*敏', '北京市昌平区北京市昌平区沙河于辛庄于辛家园1号楼1单元'],
	['郑*龙', '河南省郑州市花园路国基路花园SOHO2栋'],
	['李*', '北京市昌平区流星花园三区11号楼4单元401室'],
	['李*', '浙江省杭州市金岸提香3幢1单元1303'],
	['庄*峰', '北京市海淀区慧科大厦'],
	['马*', '北京市朝阳区惠新东街11号紫光发展大厦A座12层'],
	['朱*', '北京市海淀区东升镇宝盛东路奥北科技园领智中心Ｂ座5层'],
	['吴*峰', '湖北省武汉市幸福路鸿福花园1栋3006'],
	['付*诚', '北京市海淀区观林园'],
	['滕*', '江苏省南京市秣周东路11号双子楼9号楼15楼君度科技'],
	['石*刚', '辽宁省大连市大连市经济技术开发区福泉北路20号'],
	['程*', '北京市昌平区沙河兆丰家园'],
	['武*', '北京市昌平区回龙观西大街龙腾苑五区16号楼1单元202'],
	['郭*欣', '北京市西城区阜成门 万通新世界 B座1503'],
	['毛*', '陕西省西安市高新六路万象汇B座'],
	['龙*宇', '山东省青岛市山东省青岛市市南区青岛啤酒大厦403'],
	['郅*', '北京市顺义区后沙峪清岚花园西区15号楼一单元502'],
	['蔡*芝', '江苏省南京市新模范马路五号南京工业大学国家科技园 A2405'],
	['王*飞', '江苏省苏州市工业园区雪堂街1号，善行楼17栋'],
	['葛*光', '北京市海淀区复兴路甲23号华能大厦'],
	['胡*鑫', '天津市和平区河南路63号'],
	['陶*东', '浙江省宁波市杭州湾新区滨海四路777号b-4'],
	['王*庆', '上海市静安区万荣路700号A1 SINODIS食品有限公司'],
	['刘*闯', '北京市东城区东中街58号美惠大厦B座2单元1层MH-Z-0005'],
	['李*', '上海市闵行区航北路228弄142号202'],
	['林*春', '河南省郑州市河南中医药大学龙子湖校区'],
	['张*春', '陕西省延安市李渠镇阳山村延安北铁路小区'],
	['李*', '浙江省杭州市文三西路52号建投大厦'],
	['李*', '河南省郑州市红旗路6号华图教育'],
	['徐*麒', '河南省洛阳市河南科技大学开元校区'],
	['陈*', '江苏省苏州市伟业迎春华府'],
	['张*', '北京市北京亦庄经济开发区地泽北街1号朗致集团'],
	['伍*葵', '新疆阿克苏地区红旗坡十一队'],
	['王*操', '上海市浦东新区亮秀路72号X座6楼'],
	['孙*强', '湖北省宜昌市大学路8号三峡大学'],
	['王*军', '山东省临沂市九曲街道格瑞斯小镇'],
	['郭*', '天津市西青区侯台碧水家园e区'],
	['聂*双', '北京市海淀区柳浪家园东里5号楼3单元801室'],
	['安*', '辽宁省沈阳市青山路亚都名苑3期逸林14号楼1-11-2'],
	['戴*', '浙江省杭州市乔司街道花漫里8幢3单元101'],
	['米*俊', '陕西省西安市太白新苑'],
	['周*祺', '河南省新乡市新辉路街道建设西路保温瓶厂家属院向西100米新中批发'],
	['丁*', '山西省运城市运城宾馆对面北大青鸟'],
	['文*宇', '湖北省宜昌市三峡大学欣苑'],
	['王*', '北京市海淀区北清路68号用友软件园'],
	['张*君', '山东省青岛市上清路16号甲，青岛东软载波科技股份有限公司'],
	['正*', '山东省济南市经十路20188号'],
	['李*晓', '北京市朝阳区国际电子城总部360发票A座收发室'],
	['丁*涛', '江苏省苏州市子胥路新峰工业小区11栋苏州三川'],
	['A*yua*', '上海市浦东新区华佗路1号'],
	['夏*捷', '陕西省西安市西安邮电大学'],
	['郭*坤', '山东省济宁市济宁学院男生宿舍'],
	['杨*星', '湖北省武汉市江夏大道18号梅兰山居碧水轩'],
	['唐*宁', '新疆乌鲁木齐市新疆省乌鲁木齐头屯河区火车西站6街'],
	['田*', '上海市黄浦区马当路388号SOHO复兴广场E栋2楼R13A'],
	['覃*', '湖北省武汉市南李路55号'],
	['杨*', '北京市朝阳区光华路甲8号和侨大厦B座508'],
	['梁*雷', '北京市海淀区王庄路1号，清华同方科技广场B2006'],
	['李*', '湖北省武汉市东湖高新南湖大道182号'],
	['曹*伟', '江苏省南京市安德门大街57号楚翘城1号楼4层'],
	['郭*铠', '山西省太原市南中环西街万年花城7号楼2单元401'],
	['李*生', '江苏省南京市江山路明发3期332栋603室'],
	['许*辰', '河南省郑州市丰产路111号河南省国家税务局8楼信息中心'],
	['姚*超', '北京市昌平区TBD云集中心1号楼5层'],
	['张*', '山东省青岛市山东科技大学'],
	['高*锐', '山东省济南市经十路万科金域中心a座'],
	['严*', '安徽省合肥市双凤开发区阜阳北路与魏武路交叉口西南角北部湾小区'],
	['李*春', '山东省德州市德州职业技术学院'],
	['张*豪', '河南省南阳市河南省南阳市宛城区第七小学邮政家属院对面的楼七一搬运站'],
	['康*', '北京市朝阳区垡头东里百斯特大厦A663'],
	['陈*', '江苏省南京市文苑路9号南京邮电大学'],
	['柴*虎', '北京市昌平区北七家镇顺玮阁小区'],
	['韩*', '辽宁省葫芦岛市小庄子乡宝仓村'],
	['魏*森', '北京市昌平区于辛庄路，赋腾国创中心，2楼'],
	['邓*明', '北京市丰台区新华街三里1号楼305'],
	['赵*', '上海市宝山区宝山区高境镇高境一村11号后3号车库'],
	['徐*亮', '北京市海淀区花园东路11号泰兴大厦302'],
	['张*凡', '北京市昌平区沙河镇松兰堡迎客家园507'],
	['赵*', '北京市北京市海淀区农大国际创业园b区6065'],
	['顾*天', '北京市海淀区上地东路1号华控大厦'],
	['丁*', '上海市杨浦区安波路533弄硕和商务2号楼1102'],
	['封*号', '江苏省苏州市陆家镇陆丰东路199号水岸香堤2#2309'],
	['王*哲', '上海市静安区曲沃路430弄15号401'],
	['刘**', '湖北省武汉市左岭镇 武汉华星光电一号门'],
	['付*', '安徽省合肥市长江西路305号电信新技术楼'],
	['鲁*', '湖北省武汉市武大科技园宏业楼C座'],
	['张*', '北京市朝阳区小营路13号亚非大厦7层8704室'],
	['齐*', '湖北省武汉市珞喻路马家庄'],
	['王*', '北京市海淀区北坞嘉园北里9号楼三单元D01'],
	['陈*龙', '北京市朝阳区北卫新园'],
	['曹*生', '江苏省无锡市澄南花苑'],
	['沈*', '北京市海淀区中关村南大街甲18号北京国际大厦D座7层'],
	['续*', '山西省晋中市中都广场12层畅快车贷'],
	['赵*全', '河北省唐山市李钊庄镇大王庄村'],
	['成*', '上海市虹口区东五小区641号楼2007'],
	['方*', '上海市闵行区联航路1399弄28号1103室'],
	['曹*', '上海市浦东新区向城路15号24C'],
	['韩*德', '北京市大兴区枣园北里小区1号楼8单元202'],
	['金*鹏', '浙江省温州市温州职业技术学院生活区快递中心'],
	['陶*明', '浙江省嘉兴市南溪路桂苑小区23幢603'],
	['李*ir', '北京市丰台区南苑乡 德鑫家园9号楼5单元50'],
	['姜*杰', '山东省临沂市凤凰岭大街惠民早餐'],
	['l*xq', '辽宁省沈阳市卫工南街4-4网点2门瀚辰跆拳道'],
	['赵*', '河北省邯郸市幸福街于联防路交叉口北行幸福馨苑'],
	['张*锋', '内蒙古呼和浩特市双河镇莹昱佳苑商铺A段13号（防汛东巷莲爱粮油副食门市）'],
	['胡*', '北京市西城区鸭子桥路24号'],
	['王*鲲', '北京市延庆区东外小区15号楼一单元101'],
	['马*闻', '陕西省西安市西安邮电大学东门'],
	['许*', '安徽省合肥市宿松路紫竹苑B区2栋2单元602室'],
	['范*', '浙江省金华市金华职业技术学院'],
	['马*铎', '山西省太原市徐沟镇山西警察学院'],
	['武*文', '上海市浦东新区浦东新区盛夏路738弄樟盛苑32号楼一楼'],
	['陈*', '江苏省徐州市苏堤北小区四号楼三单元702室'],
	['曹*政', '辽宁省大连市大连理工大学软件学院'],
	['张*超', '山东省济南市八一立交桥西南角联通公司3号楼'],
	['唐*生', '山东省济南市工业南路鑫苑国际城市花园'],
	['严*鹏', '上海市杨浦区五角场街道 国定路277弄铁村小区13号601'],
	['张**', '甘肃省兰州市甘肃省兰州市七里河区兰公坪兰州理工大学校本部'],
	['麻*肖', '安徽省宿州市香格里拉108幢'],
	['刘*仪', '河北省廊坊市燕郊经济开发区 华北科技学院'],
	['刘*龙', '河南省洛阳市新一中文印室'],
	['李*', '陕西省西安市临潼区西安科技大学'],
	['相**', '北京市昌平区天通公园里'],
	['康*熙', '山西省忻州市万人商厦对面联想专卖店'],
	['张*栋', '山东省泰安市安驾庄镇上前'],
	['陶*', '安徽省宣城市鳌峰东路180号宣城皖南农商银行413室'],
	['艾*麦提江·拜克热', '浙江省杭州市浦沿街道江畔云卢4幢2单元1202'],
	['王*', '上海市浦东新区福山路455号，全华信息大厦，1楼，平安银行'],
	['刘*林', '湖北省宜昌市枝城镇大堰村四组'],
	['罗*', '河南省信阳市西关黄国新城C6'],
	['莫*', '河南省郑州市金水区76号9202'],
	['徐*龙', '安徽省合肥市长江西路新加坡花园城4联排'],
	['杨*杰', '山西省忻州市京原南路雷神网咖'],
	['朱*北', '海南省海口市和平北路三亚上二街9号'],
	['朱*', '浙江省杭州市龙湖春江郦城'],
	['常*磊', '北京市海淀区学院南路59号'],
	['王*阳', '江苏省南京市南京江宁21世纪现代城'],
	['谢*星', '甘肃省酒泉市雄关路54号东风物流十号'],
	['侯*', '河南省郑州市河南省郑州市高新区莲花街牡丹路西雅图荣邦城'],
	['孙*康', '江苏省南京市化工园方水东路9号'],
	['索*华', '北京市昌平区北七家镇东三旗村委会'],
	['王*', '陕西省西安市十里铺街长力小区北门对面（王家辣子面）'],
	['姜*生', '北京市朝阳区东大桥宫宵国际1103'],
	['顾*生', '安徽省阜阳市清河西路100号阜阳师范学院'],
	['申*伟', '上海市青浦区巷佳华苑三期10号楼904室'],
	['刘*', '湖北省武汉市左岭新城1社区15栋'],
	['单*成', '山东省日照市日照职业技术学院'],
	['韩*红', '上海市杨浦区隆昌路619号10号楼二楼'],
	['魏*琪', '北京市丰台区汉威国际广场4区12号楼'],
	['杨*康', '北京市丰台区丰台科技园汉威广场12栋']
]

special_list = {
    "内蒙":"内蒙古自治区",
    "广西":"广西壮族自治行政区",
    "西藏":"西藏自治区",
    "宁夏":"宁夏回族自治区",
    "澳门":"澳门特别行政区",
    "新疆":"新疆维吾尔自治区",
    "香港":"香港特别行政区",
    "黑龙":"黑龙江省"
}

result = {}
for item in pos_list:
    pro = item[1][:2]
    special = special_list.get(pro)
    if special:
        pro = special

    if pro in result:
        result[pro].append(item)
    else:
        result[pro] = [item]
print(result)

for k,v in result.items():
    print(k,len(v))