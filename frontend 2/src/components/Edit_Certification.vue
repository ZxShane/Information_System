<template>
  <div>
    <h1 align="center">填写考证信息</h1>
    <!-- <div class="box"> -->
    <div style="background: #ffe4e1; padding: 20px; margin-top: 20px">
      <Card :bordered="false">
        <Form
          ref="formValidate"
          :model="formValidate"
          :rules="ruleValidate"
          :label-width="80"
        >
          <FormItem label="姓名" prop="name">
            <Input
              v-model="formValidate.name"
              :placeholder="formValidate.name"
            ></Input>
          </FormItem>
          <FormItem label="邮箱" prop="mail">
            <Input
              v-model="formValidate.mail"
              :placeholder="formValidate.mail"
            ></Input>
          </FormItem>
          <FormItem label="证书名称" prop="certification_name">
            <Input
              v-model="formValidate.certification_name"
              :placeholder="certification_name"
            ></Input>
          </FormItem>
          <FormItem label="相关网址" prop="link">
            <Input
              v-model="formValidate.link"
              :placeholder="formValidate.link"
            ></Input>
          </FormItem>
          <FormItem label="简介" prop="introduction">
            <Input
              v-model="formValidate.introduction"
              type="textarea"
              :autosize="{ minRows: 2, maxRows: 5 }"
              :placeholder="formValidate.introduction"
            ></Input>
          </FormItem>
          <FormItem>
            <Button type="primary" @click="handleSubmit('formValidate')"
              >提交</Button
            >
            <Button
              @click="handleReset('formValidate')"
              style="margin-left: 8px"
              >重置</Button
            >
          </FormItem>
        </Form>
      </Card>
    </div>
  </div>
  <!-- </div> -->
</template>
<script>
export default {
  name:'editcertification',
  data() {
    return {
      certification_id:'',
      formValidate: {
        name: "",
        mail: "",
        certification_name: "",
        link: "",
        introduction: "",
      },
      ruleValidate: {
        name: [{ required: true, message: "姓名不能为空", trigger: "blur" }],
        mail: [
          { required: true, message: "电子邮箱不能为空", trigger: "blur" },
          { type: "email", message: "格式错误", trigger: "blur" },
        ],

        certification_name: [
          { required: true, message: "课程名称不能为空", trigger: "change" },
        ],
        link: [
          { required: true, message: "请填写授课教师", trigger: "change" },
        ],

        introduction: [
          { required: true, message: "请填写简介", trigger: "blur" },
          { type: "string", min: 5, message: "不能少于5字", trigger: "blur" },
        ],
      },
    };
  },
  created(){
            this.certification_id = this.$route.params.certification_id
           
            this.showcertification()
        },
  methods: {
    showcertification(){
        let self = this
                this.$axios.get('/api/show_one_certification/',{
                    params:{
                        certification_id:self.certification_id
                    }
                }).then((res)=>{
                    console.log(res.data)
                    self.formValidate.name=res.data.list[0].fields.publisher
                    self.formValidate.mail = res.data.list[0].fields.publisher_email
                    self.formValidate.certification_name = res.data.list[0].fields.certification_name
                    self.formValidate.link = res.data.list[0].fields.link
                    self.formValidate.introduction = res.data.list[0].fields.introduction
                })
            },
    handleSubmit(name) {
      let self = this;
      // t=
     
      this.$refs[name].validate((valid) => {
        if (valid) {
          // this.$Message.success('Success!');
          console.log(self.formValidate);
          this.$axios
            .get("/api/change_certification/", {
              params: {
                // user_nubmer: '01',
                certification_id: self.certification_id,
                publisher: self.formValidate.name,
                publisher_email: self.formValidate.mail,
                certification_name: self.formValidate.certification_name,
                link: self.formValidate.link,
                introduction: self.formValidate.introduction,
                // ischeck: "0",
              },
            })
            .then((res) => {
              console.log(res.data);
              if (res.data.msg == "success") {
                alert("提交成功！")
                 this.$router.go(-1)
              } else {
                this.$Message.error("信息填写错误，请仔细检查");
              }
            });
          // console.log(this.formValidate)
        } else {
          this.$Message.error("Fail!");
        }
      });
    },
    handleReset(name) {
      this.$refs[name].resetFields();
    },
  },
};
</script>

