<template>
<div>
    <h1 align='center'>填写书籍</h1>
<!-- <div class="box"> -->
    <div style="background:	#E6E6FA;padding: 20px; margin-top:20px;">
        <Card :bordered="false">
    <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="80">
        <FormItem label="姓名" prop="name">
            <Input v-model="formValidate.name" :placeholder="formValidate.name"></Input>
        </FormItem>
        <FormItem label="邮箱" prop="mail">
            <Input v-model="formValidate.mail" :placeholder="formValidate.mail"></Input>
        </FormItem>
        <FormItem label="书名" prop="book_name">
            <Input v-model="formValidate.book_name" :placeholder="formValidate.book_name"></Input>
        </FormItem>
        <FormItem label="作者" prop="author">
            <Input v-model="formValidate.author" :placeholder="formValidate.author"></Input>
        </FormItem>
        <FormItem label="类型" prop="type">
            <RadioGroup v-model="formValidate.type"  >
                <Radio label="教材"></Radio>
                <Radio label="小说"></Radio>
                <Radio label="社科"></Radio>
                <Radio label="科技"></Radio>
            </RadioGroup>
        </FormItem>
        <FormItem label="简介" prop="introduction">
            <Input v-model="formValidate.introduction" type="textarea" :autosize="{minRows: 2,maxRows: 5}" :placeholder="formValidate.introduction"></Input>
        </FormItem>
        <FormItem>
            <Button type="primary" @click="handleSubmit('formValidate')">提交</Button>
            <!-- <Button @click="handleReset('formValidate')" style="margin-left: 8px">重置</Button> -->
        </FormItem>
    </Form>
            </Card>
    </div>
</div>
    <!-- </div> -->
</template>
<script>
    export default {
        name:'editbook',
        data () {
            return {
                book_id:'',
                // user_name:'',
                // user_mail:'',
                // book_name:'',
                // author:'',
                // type:'',
                // introduction:'',
                formValidate: {
                    // user_name: '',
                    name:'',
                    mail: '',
                    author: '',
                    type: '',
                    book_name:'',
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
                    book_name: [
                        { required: true, message: '请填写书籍名称', trigger: 'change' }
                    ],
                    author: [
                        { required: true, message: '请填写书籍作者', trigger: 'change' }
                    ],
                    
                    
                    introduction: [
                        { required: true, message: '请填写简介', trigger: 'blur' },
                        { type: 'string', min: 10, message: '不能少于10字', trigger: 'blur' }
                    ]
                }
            }
        },
        created(){
            this.book_id = this.$route.params.book_id
            console.log(this.book_id)
            // this.book_id="2021050820228"
            this.showbook()
        },
        methods: {
            showbook(){
                let self = this
                this.$axios.get('/api/show_one_book/',{
                    params:{
                        book_id:self.book_id
                    }
                }).then((res)=>{
                    console.log(res.data)
                    self.formValidate.name=res.data.list[0].fields.publisher
                    self.formValidate.mail = res.data.list[0].fields.publisher_email
                    self.formValidate.author = res.data.list[0].fields.author
                    self.formValidate.type = res.data.list[0].fields.type
                    self.formValidate.book_name = res.data.list[0].fields.book_name
                    self.formValidate.introduction = res.data.list[0].fields.introduction


                })
            },
            handleSubmit (name) {
                let self=this
                // t=
                // console.log(this.getNowFormatDate())
                this.$refs[name].validate((valid) => {
                    if (valid) {
                        // this.$Message.success('Success!');
                        console.log(self.formValidate)
                        this.$axios.get('/api/change_book/',{
                    params:{
                        // user_nubmer: '01',
                        book_id:self.book_id,
                        publisher: self.formValidate.name,
                        publisher_email : self.formValidate.mail,
                        book_name :self.formValidate.book_name,
                        author : self.formValidate.author,
                        type: self.formValidate.type,
                        introduction:self.formValidate.introduction,
                        // ischeck:'0'
                    }
                }).then((res)=>{
                    console.log(res.data)
                    if(res.data.msg == "success"){
                        alert('提交成功！');
                        this.$router.go(-1)
                    }else{
                        this.$Message.error("信息填写错误，请仔细检查");
                    }
                })
                        // console.log(this.formValidate)
                    } else {
                         
                        this.$Message.error('Fail!');
                       
                    }
                })
                
                
            },
            handleReset (name) {
                this.$refs[name].resetFields();
            },
            
        }
    }
</script>
<style scoped>
.box{
    

}
</style>
