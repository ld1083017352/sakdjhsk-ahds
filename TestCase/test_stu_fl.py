import  allure
import  pytest
from  Common import  Request,Assert,read_excel
request=Request.Request()
assertions =Assert.Assertions()
head={}
fl_id = 0
@allure.feature("商品分类模块")
class Test_info:
    @allure.story("登录接口")
    def test_login(self):
        login_resp = request.post_request(url='http://192.168.60.132:8080/admin/login',
                                          json={"username": "admin", "password": "123456"})
        assertions.assert_code(login_resp.status_code, 200)


        login_resp_json = login_resp.json()

        assertions.assert_in_text(login_resp_json['message'], '成功')
        data_json=login_resp_json['data']
        token=data_json['tokenHead']+data_json['token']
        print(token)
        global  head
        head={'Authorization':token}
    @allure.story("获取商品分类")
    def test_sel(self):
        fenlei=request.get_request(url='http://192.168.60.132:8080/productCategory/list/0',
                            params={'pageNum': 1, 'pageSize': 5},headers=head)
        assertions.assert_code(fenlei.status_code, 200)
        feilei_resp_json = fenlei.json()
        assertions.assert_in_text(feilei_resp_json['message'], '成功')
        resp_data = feilei_resp_json['data']
        data_list = resp_data['list']
        fl_dict = data_list[0]
        global fl_id
        fl_id = fl_dict['id']

    @allure.story("删除商品分类")
    def test_del(self):
      dell=request.post_request(url='http://192.168.60.132:8080/productCategory/delete/'+str(fl_id),
                                headers=head)
      assertions.assert_code(dell.status_code, 200)
      dell_json = dell.json()
      assertions.assert_in_text(dell_json['message'], '成功')


    @allure.story("添加商品分类")
    def test_add(self):
        adaa=request.post_request(url='http://192.168.60.132:8080/productCategory/create',
                               json={"description": "", "icon": "", "keywords": "", "name": "家电",
                                                  "navStatus": 0, "parentId": 0, "productUnit": "", "showStatus": 0,
                                                  "sort": 0, "productAttributeIdList":[]
                                     },headers=head)

        assertions.assert_code(adaa.status_code, 200)
        login_resp_json = adaa.json()
        assertions.assert_in_text(login_resp_json['message'], '成功')