<template>
<div>
    <h1 align='center'>填写毕业生去向</h1>
<!-- <div class="box"> -->
    <div style="background:#FFF0F5;padding: 20px; margin-top:20px;">
        <Card :bordered="false">
    <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="80">
        <FormItem label="姓名" prop="name">
            <Input v-model="formValidate.name" :placeholder="formValidate.name"></Input>
        </FormItem>
        <FormItem label="邮箱" prop="mail">
            <Input v-model="formValidate.mail" :placeholder="formValidate.mail"></Input>
        </FormItem>
        <FormItem label="类型" prop="type">
            <RadioGroup v-model="formValidate.type">
                <Radio label="升学（保研/考研）"></Radio>
                <Radio label="出国深造"></Radio>
                <Radio label="就业"></Radio>
                <Radio label="其他"></Radio>
            </RadioGroup>
        </FormItem>
        <FormItem label="接收单位" prop="destination_department">
            <Input v-model="formValidate.destination_department" :placeholder="formValidate.destination_department"></Input>
        </FormItem>
        <!-- <FormItem label="简介" prop="introduction">
            <Input v-model="formValidate.introduction" type="textarea" :autosize="{minRows: 2,maxRows: 5}" placeholder="单位简介"></Input>
        </FormItem> -->
        <FormItem >
            <Button type="primary" @click="handleSubmit('formValidate')">提交</Button>
           
        </FormItem>
    </Form>
            </Card>
    </div>
</div>
    <!-- </div> -->
</template>
<script>
    export default {
      name:'editdestination',
        data () {
            return {
                formValidate: {
                    name: '',
                    mail: '',
                    type: '',
                    destination_department:'',
                    // introduction:''
                },
                ruleValidate: {
                    name: [
                        { required: true, message: '姓名不能为空', trigger: 'blur' }
                    ],
                    mail: [
                        { required: true, message: '电子邮箱不能为空', trigger: 'blur' },
                        { type: 'email', message: '格式错误', trigger: 'blur' }
                    ],
                    type: [
                        { required: true, message: '请选择一个类型', trigger: 'change' }
                    ],
                    
                    
                    destination_department: [
                        { required: true, message: '请填写接收单位', trigger: 'change' }
                    ],
                    
                    
                    introduction: [
                        { required: true, message: '请填写简介', trigger: 'blur' },
                        { type: 'string', min: 5, message: '不能少于5字', trigger: 'blur' }
                    ]
                }
            }
        },
        created(){
            this.user_number = this.$route.params.user_number
            // this.user_number="2008001"
            this.showdestination()
        },
        methods: {
            showdestination(){
                let self = this
                this.$axios.get('/api/show_one_destination/',{
                    params:{
                        user_number:self.user_number
                    }
                }).then((res)=>{
                    console.log(res.data)
                    self.formValidate.name=res.data.list[0].fields.user_name
                    self.formValidate.mail = res.data.list[0].fields.user_email
                    
                    self.formValidate.type = res.data.list[0].fields.type
                    self.formValidate.destination_department = res.data.list[0].fields.destination_info
                    // self.formValidate.introduction = res.data.list[0].fields.introduction


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
            .get("/api/change_destination/", {
              params: {
                // user_nubmer: '01',
                user_number: self.user_number,
                user_name: self.formValidate.name,
                user_email: self.formValidate.mail,
                type: self.formValidate.type,
                destination_info: self.formValidate.destination_department,
                // introduction: self.formValidate.introduction,
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
            handleReset (name) {
                this.$refs[name].resetFields();
            }
        }
    }
</script>

