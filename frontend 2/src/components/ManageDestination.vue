<template>
<div>
<div v-show="!isshow">
<h1 align="center">毕业生去向审核</h1>
    <Table border :columns="columns12" :data="data6">
        <template slot-scope="{ row }" slot="name">
            <strong>{{ row.name }}</strong>
        </template>
        <template slot-scope="{ row, index }" slot="action">
            <Button type="primary" size="small" style="margin-right: 5px" @click="edit(index)">编辑</Button>
            <Button type="error" size="small" @click="check(index,'1')">通过</Button>
            <Button type="error" size="small" @click="check(index,'0')">不通过</Button>
            <!-- <Button type="error" size="small" @click="remove(index)">Delete</Button> -->
        </template>
    </Table>
</div>

<div v-show="isshow">
    <h1 align='center'>填写毕业生去向</h1>
<!-- <div class="box"> -->
    <div style="background:#FFF0F5;padding: 20px; margin-top:20px;">
        <Card :bordered="false">
    <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="80">
        <FormItem label="姓名" prop="name">
            <Input v-model="formValidate.name" placeholder="填写您的姓名"></Input>
        </FormItem>
        <FormItem label="邮箱" prop="mail">
            <Input v-model="formValidate.mail" placeholder="填写您的邮箱"></Input>
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
            <Input v-model="formValidate.destination_department" placeholder="学校/单位"></Input>
        </FormItem>
        <FormItem label="简介" prop="introduction">
            <Input v-model="formValidate.introduction" type="textarea" :autosize="{minRows: 2,maxRows: 5}" placeholder="单位简介"></Input>
        </FormItem>
        <FormItem >
            <Button type="primary" @click="handleSubmit('formValidate')">提交</Button>
            <Button @click="handleReset('formValidate')" style="margin-left: 8px">重置</Button>
        </FormItem>
    </Form>
            </Card>
    </div>
</div>
    </div>
</template>

<script>
    export default {
        data () {
            return {
                user_number:'',
                isshow:false,
                columns12: [
                    // {
                    //     title: '学号',
                    //     slot: 'user_number'
                    // },
                    {
                        title: '姓名',
                        key: 'user_name'
                    },
                    {
                        title: '毕业去向',
                        key: 'destination_info'
                    },
                    {
                        title: '联系方式',
                        key: 'user_email'
                    },
                    {
                        title: '审核结果',
                        key: 'ischeck'
                    },
                    {
                        title: '查看',
                        slot: 'action',
                        width: 200,
                        align: 'center'
                    }
                ],
                data:[],
                key:[],
                k:'',
                data6: [],
                formValidate: {
                    name: '',
                    mail: '',
                    type: '',
                    destination_department:'',
                    introduction:''
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
            this.user_number=window.sessionStorage.getItem('user_number')
            this.class = window.sessionStorage.getItem('user_class')
            console.log(this.class)
            if(this.class=='0'){
                this.isshow=true
            }else if(this.class=='2'){
                this.getallcourse()
            }else{
                alert('暂无管理权限！')
                this.$router.push({
                    path:'/showdestination'
                })
            }
            
            
        },
        methods: {
            show (index) {
                this.$Modal.info({
                    title: '毕业去向',
                    content: `姓名：${this.data[index].fields.user_name}<br>学号：${this.data[index].pk}<br>毕业去向：${this.data[index].fields.destination_info}`
                })
            },
            remove (index) {
                this.data6.splice(index, 1);
            },
            check (index,ischeck) {
                this.k=this.key[index]
                console.log(this.k)
                let self = this
                this.$axios.get('/api/check_destination/',{
                   params:{
                       user_number: self.k,
                       ischeck:ischeck
                   }
                }).then(res=>{
                    console.log(res.data.list)
                    console.log(ischeck)
                    console.log(this.k)
                    window.location.reload()
                })

            },
            getallcourse(){
            let self = this
            this.$axios.get('/api/show_all_destinations/').then(res=>{
              console.log(res.data.list)
              self.data=res.data.list
              for (var i =0;i<res.data.list.length;i++){
                  self.data6.push(res.data.list[i].fields)
                  self.key.push(res.data.list[i].pk)
                  
              }
            //   self.data6 = res.data.list
            console.log(self.data6)
        })
        },
        getNowFormatDate() {
      var date = new Date();
      // var seperator1 = "-";
      var year = date.getFullYear();
      var month = date.getMonth() + 1;
      var strDate = date.getDate();
      var h = date.getHours(); //获取当前小时数(0-23)
      var m = date.getMinutes(); //获取当前分钟数(0-59)
      var s = date.getSeconds();
      if (month >= 1 && month <= 9) {
        month = "0" + month;
      }
      if (strDate >= 0 && strDate <= 9) {
        strDate = "0" + strDate;
      }
      var currentdate = year + month + strDate + h + m + s;
      return currentdate;
    },

    handleSubmit(name) {
      let self = this;
      // t=
      console.log(this.getNowFormatDate());
      this.$refs[name].validate((valid) => {
        if (valid) {
          // this.$Message.success('Success!');
          console.log(self.formValidate);
          this.$axios
            .get("/api/add_destination/", {
              params: {
                // user_nubmer: '01',
                user_number: self.user_number,
                user_name: self.formValidate.name,
                user_email: self.formValidate.mail,
                type: self.formValidate.type,
                destination_info: self.formValidate.destination_department,
                introduction: self.formValidate.introduction,
                ischeck: "0",
              },
            })
            .then((res) => {
              console.log(res.data);
              if (res.data.msg == "success") {
                alert("提交成功！")
                window.location.reload();
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
            },
            edit(index){
                this.k=this.data[index].pk
                console.log(this.k)
                this.$router.push({
                    name:'EditDestination',
                    params:{
                        user_number: this.k
                    }
                })
            }
        }
        
    
    }
</script>
