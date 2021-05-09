<template>
  <div id="personalinfo">
    <i-form :label-width="80">
      <h2>基本信息</h2>
      <br />
      <Form-item label="学号*">
        <i-input v-model="user_number" :placeholder="user_number" disabled></i-input>
      </Form-item>
      <Form-item label="用户名">
        <i-input v-model="user_id" :placeholder="user_id"></i-input>
      </Form-item>
      <Form-item label="真实姓名">
        <i-input v-model="user_name" :placeholder="user_name"></i-input>
      </Form-item>
      <Form-item label="密码">
        <i-input v-model="user_password" :placeholder="user_password"></i-input>
      </Form-item>
      <Form-item label="性别">
        <RadioGroup v-model="user_gender">
          <Radio label="男"></Radio>
          <Radio label="女"></Radio>
        </RadioGroup>
      </Form-item>
      <FormItem label="类型" prop="type">
            <RadioGroup v-model="user_class">
                <Radio label="在校生"></Radio>
                <Radio label="毕业生"></Radio>
            </RadioGroup>
        </FormItem>
      
        <i-button type="primary" @click="handleSubmit()">保存</i-button>
        <!-- <i-button type="ghost" @click="handleReset('formValidate')" style="margin-left: 8px ;color:black;">重置</i-button>  -->
      
    </i-form>
  </div>
</template>
<script>

export default {
  name: "personalinfo",
  data() {
    return {
     user_number:'',
     user_id:'',
     user_name:'',
     user_password:'',
     user_gender:'',
     user_class:''
    };
  },
  created() {
   
    this.user_number = window.sessionStorage.getItem('user_number')
    //this.getinfo()
    this.showcertification()
  },
  methods: {
      showcertification(){
        let self = this
                this.$axios.get('/api/show_one_user/',{
                    params:{
                        user_number:self.user_number
                    }
                }).then((res)=>{
                    console.log(res.data)
                    self.user_name=res.data.list[0].fields.user_name
                    self.user_id = res.data.list[0].fields.user_id
                    self.user_password=res.data.list[0].fields.user_password
                    self.user_gender = res.data.list[0].fields.user_gender
                    if(res.data.list[0].fields.user_class=='0'){
                        self.user_class="毕业生"
                    }else if(res.data.list[0].fields.user_class=='1'){
                        self.user_class="在校生"
                    }
                    
                })
            },
    handleSubmit() {
      let self = this;
      if(self.user_class=="在校生"){
        var type='1'
      }else if(self.user_class=="毕业生"){
        var type='0'
      }

      this.$axios
        .get("/api/change_user/", {
          params: {
            user_number:self.user_number,
            user_id: self.user_id,
            user_name:self.user_name,
            user_password:self.user_password,
            user_gender:self.user_gender,
            user_class:type
          }
        })
        .then(res => {
          console.log(res.data)
          alert("修改成功")
          self.$router.go(-1)
        //   if (res.data.error_num == 1) {
        //     console.log(self.name);
        //     alert("创建失败,错误：" + res.data.msg);
        //     console.log(res);
        //   } else {
        //     alert("创建成功！");
        //     console.log(res);
        //     self.$router.push({
        //     name:'CreateNewcase',
        //     params:{
        //       stu_num:self.stu_num
        //     }
        // })
          // }
        });
    },
    add(info) {
      this.doctordate.push(info);
    }
  }
};
</script>
