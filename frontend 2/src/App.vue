<template>
  <div id="app">
    <div class="layout">
      <Layout>
        <Header style="background-color:#87CEFA;">
          <p style="color:black;text-align:center;font-size:30px;font-weight:700;letter-spacing:20px;">学生信息管理系统</p>
        </Header>
        <Layout>
          <Sider hide-trigger :style="{background: '#fff'}">
            <Menu active-name="1-2" theme="light" width="auto" :open-names="['1']">
             <router-link to ="showinfo"> <MenuItem name="4-1"><Icon type="ios-analytics"></Icon>个人中心</MenuItem></router-link>
              <Submenu name="1">
                <template slot="title">
                  <Icon type="ios-navigate"></Icon>书籍模块
                </template>
                <router-link to ="showbook"><MenuItem name="1-1">书籍信息</MenuItem></router-link>
                <router-link to ="managebook"><MenuItem name="1-2">管理书籍</MenuItem></router-link>
                <!-- <router-link to ="applybook"><MenuItem name="1-3">书籍申请</MenuItem></router-link> -->
                <!-- <router-link to ="evaluate"><MenuItem name="1-3">班级互评</MenuItem></router-link> -->
              </Submenu>
              <Submenu name="2">
                <template slot="title">
                  <Icon type="ios-keypad"></Icon>幕课信息
                </template>
                <router-link to ="showcourse"><MenuItem name="2-1">幕课信息</MenuItem></router-link>
                <router-link to ="managecourse"><MenuItem name="2-2">幕课管理</MenuItem></router-link>
                <!-- <router-link to ="applycourse"><MenuItem name="2-3">幕课申请</MenuItem></router-link> -->
              </Submenu>
              <Submenu name="3">
                <template slot="title">
                  <Icon type="ios-navigate"></Icon>毕业生去向
                </template>
                <router-link to ="showdestination"><MenuItem name="3-1">毕业生去向汇总</MenuItem></router-link>
                <router-link to ="managedestination"><MenuItem name="3-2">毕业生去向管理</MenuItem></router-link>
                <!-- <router-link to ="applydestination"><MenuItem name="3-3">毕业生去向申请</MenuItem></router-link> -->
              </Submenu>
              <Submenu name="4">
                <template slot="title">
                  <Icon type="ios-keypad"></Icon>考证模块
                </template>
                <router-link to ="showcertification"><MenuItem name="4-1">考证信息汇总</MenuItem></router-link>
                <router-link to ="managecertification"><MenuItem name="4-2">考证信息管理</MenuItem></router-link>
                <!-- <router-link to ="applycertification"><MenuItem name="4-3">考证信息申请</MenuItem></router-link> -->
              </Submenu>
            </Menu>
          </Sider>
          <Layout :style="{padding: '0 24px 24px',overflow:'auto'}">
            <Content :style="{padding: '24px', minHeight: '650px', background: '#fff',overflow:'visible'}">
              <router-view />
            </Content>
          </Layout>
        </Layout>
      </Layout>
    </div>
  </div>
</template>
<script>
export default {};
</script>
<style scoped>
.layout {
  border: 1px solid #d7dde4;
  background: #f5f7f9;
  position: relative;
  border-radius: 4px;
  height: 800px;
}
.layout-logo {
  width: 100px;
  height: 30px;
  background: #5b6270;
  border-radius: 3px;
  float: left;
  position: relative;
  top: 15px;
  left: 20px;
}
.layout-nav {
  width: 420px;
  margin: 0 auto;
  margin-right: 20px;
  background-color: #90EE90;
}
a{
  color:#5b6270;
}
</style>

