<template>
<div>
    <h1 align='center'>填写幕课</h1>
<!-- <div class="box"> -->
    <div style="background:#F0F8FF;padding: 20px; margin-top:20px;">
        <Card :bordered="false">
    <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="80">
        <FormItem label="姓名" prop="name">
            <Input v-model="formValidate.name" :placeholder="formValidate.name"></Input>
        </FormItem>
        <FormItem label="邮箱" prop="mail">
            <Input v-model="formValidate.mail" :placeholder="formValidate.mail"></Input>
        </FormItem>
        <FormItem label="课程名称" prop="course_name">
            <Input v-model="formValidate.course_name" :placeholder="formValidate.course_name"></Input>
        </FormItem>
        <FormItem label="授课教师" prop="teacher">
            <Input v-model="formValidate.teacher" :placeholder="formValidate.teacher"></Input>
        </FormItem>
        <FormItem label="类型" prop="type">
            <RadioGroup v-model="formValidate.type">
                <Radio label="必修课"></Radio>
                <Radio label="专业选修课"></Radio>
                <Radio label="公共选修课"></Radio>
                <Radio label="兴趣课"></Radio>
            </RadioGroup>
        </FormItem>
        <FormItem label="教材" prop="book">
            <Input v-model="formValidate.book" :placeholder="formValidate.book"></Input>
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
        name:'editcourse',
        data () {
            return {
                formValidate: {
                    name: '',
                    mail: '',
                    course_name: '',
                    teacher: '',
                    type: '',
                    book:'',
                    // time: '',
                    introduction: ''
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
                    course_name: [
                        { required: true, message: '课程名称不能为空', trigger: 'blur' }
                    ],
                    teacher: [
                        { required: true, message: '请填写授课教师', trigger: 'blur' }
                    ],
                    
                    book: [
                        { required: true, message: '请填写课程教材', trigger: 'blur' }
                    ],
                    
                    
                    introduction: [
          { required: true, message: "请填写简介", trigger: "blur" },
          { type: "string", min: 5, message: "不能少于5字", trigger: "blur" },
        ],
                }
            }
        },
        created(){
            this.course_id = this.$route.params.course_id
            // this.course_id="02"
            this.showcourse()
        },
        methods: {
            showcourse(){
        let self = this
                this.$axios.get('/api/show_one_course/',{
                    params:{
                        course_id:self.course_id
                    }
                }).then((res)=>{
                    console.log(res.data)
                    self.formValidate.name=res.data.list[0].fields.publisher
                    self.formValidate.mail = res.data.list[0].fields.publisher_email
                    self.formValidate.course_name = res.data.list[0].fields.course_name
                    self.formValidate.book = res.data.list[0].fields.book
                    self.formValidate.type = res.data.list[0].fields.type
                    self.formValidate.teacher = res.data.list[0].fields.teacher
                    self.formValidate.introduction = res.data.list[0].fields.introduction
                })
            },
    handleSubmit(name) {
      let self = this;
      // t=
    //   console.log(this.getNowFormatDate());
      this.$refs[name].validate((valid) => {
        if (valid) {
          // this.$Message.success('Success!');
          console.log(self.formValidate);
          this.$axios
            .get("/api/change_course/", {
              params: {
                // user_nubmer: '01',
                course_id: self.course_id,
                publisher: self.formValidate.name,
                publisher_email: self.formValidate.mail,
                course_name: self.formValidate.course_name,
                teacher: self.formValidate.teacher,
                book: self.formValidate.book,
                type:self.formValidate.type,
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
            handleReset (name) {
                this.$refs[name].resetFields();
            }
        }
    }
</script>

