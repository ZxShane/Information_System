<template>
  <div id="load">
    <h1 style="margin-left:20%;margin-bottom:10%;">登录</h1>
    <i-form inline>
      <!-- <Form-item>
        <h4 style="block:inline;">用户名：</h4>
        <i-input type="text" placeholder="用户名" inline margin-bottom="10%" v-model="userid">
          <Icon type="ios-person-outline" slot="prepend"></Icon>
        </i-input>
      </Form-item>
      <br />-->
      <Form-item> 
        <h4 style="block:inline;">学 号</h4>
        <i-input type="text" placeholder="学号" inline margin-bottom="10%" v-model="usernumber">
          <Icon type="ios-person-outline" slot="prepend"></Icon>
        </i-input>
      </Form-item>
      <br />
      <Form-item>
        <h4 style="block:inline;">密码：</h4>
        <i-input type="password" placeholder="密码" inline v-model="userpassword">
          <Icon type="ios-pin-outline" slot="prepend"></Icon>
        </i-input>
      </Form-item>
      <br />
      <Form-item style="margin-top:3%;">
        <i-button type="primary" @click="handleSubmit()" style="margin-left:130px;">登录</i-button>
        <i-button type="primary" @click="register()" >注册</i-button>
      </Form-item>
    </i-form>
  </div>
</template>
<script>
export default {
  name: "Load",
  data() {
    return {
      // username: "",
      userpassword: "",
      userid:'',
      usernumber:'',
      stu_num: ""
    };
  },
  created() {
    
  },
  methods: {
    handleSubmit() {
      let self = this;
      // var type=''
      // var num=
      // console.log(self.usernumber)
      this.$axios
        .get("/api/show_one_user/",{
          params:{
              user_number: self.usernumber
          }
          
        }).then(res => {
           console.log(res.data);
          if(res.data.list==''){
            alert("学号尚未注册！")
          }else if(res.data.list[0].fields.user_password != self.userpassword){
            alert('学号或密码错误！')
          }
          else{
            window.sessionStorage.setItem('user_number',self.usernumber)
            window.sessionStorage.setItem('user_class',res.data.list[0].fields.user_class)
            self.$router.push({
            path:'/showinfo'
        })
         
          
          }
          // if (self.username==self.password){
          //  window.sessionStorage.setItem('stu_num',self.username)
          //  self.$router.push({
          //   path:'/createnewcase'
          // })
          // }else{
          //   alert("账号或密码错误！")
          // }
        })

      // this.$axios.post("http://117.78.1.3:8080/invoke",{
      //   func:'doctorLogin',
      //   username:self.username,
      //   password:self.password
      // }).then((res)=>{
      //   self.doctorId = res.data
      //   console.log(res)
      //   window.sessionStorage.setItem('doctorId',res.data)
      //   self.$router.push({
      //     path:'/createnewcase'
      //   })
      // })
    },
    register() {
      this.$router.push({
        name: "PersonalInfo"
      });
    }
  }
};
</script>
<style scoped>
#load {
  margin-top: 70px;
  /* border-style: solid;
  border-color: cornflowerblue; */
  border-radius: 10px;
  margin-left: 30%;
  margin-right: 40%;
  padding-left: 5%;
  padding-right: 2%;
}
</style>
