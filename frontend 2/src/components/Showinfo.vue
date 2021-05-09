<template>
  <div id="showinfo" style="overflow:auto;">
    <h1>{{user_id}},您好！</h1>
    <div style="margin-bottom:20px;margin-top:30px;">
    <p style="color:#87CEFA;font-weight:900;font-size:20px;">个人信息</p>
    <hr style=" height:2px;border:none;border-top:2px dotted #87CEFA;margin-bottom:20px;" />
      <h2>姓名: &nbsp;{{ user_name }}，学号: &nbsp;{{ user_number }}</h2>
      <h2 >性别:&nbsp;{{user_gender}}，学生类别:&nbsp;{{ user_type }}</h2>
    
    </div>
    <Button type="primary" @click="editinfo()">修改</Button>
    <p style="color:#87CEFA;font-weight:900;font-size:20px;margin-top:20px;">书籍申请</p>
    <hr style=" height:2px;border:none;border-top:2px dotted #87CEFA;margin-bottom:20px;" />
      <Table border :columns="columnsbook" :data="databook">
        <template slot-scope="{ row }" slot="name">
            <strong>{{ row.name }}</strong>
        </template>
        <template slot-scope="{ row, index }" slot="action">
            <!-- <Button type="primary" size="small" style="margin-right: 5px" @click="show(index)">查看</Button> -->
            <Button type="error" size="small" @click="editbook(index)">修改</Button>
            
            <!-- <Button type="error" size="small" @click="remove(index)">Delete</Button> -->
        </template>
    </Table>
    <p style="color:#87CEFA;font-weight:900;font-size:20px;margin-top:20px;">幕课申请</p>
    <hr style=" height:2px;border:none;border-top:2px dotted #87CEFA;margin-bottom:20px;" />
    <Table border :columns="columnscourse" :data="datacourse">
        <template slot-scope="{ row }" slot="name">
            <strong>{{ row.name }}</strong>
        </template>
        <template slot-scope="{ row, index }" slot="action">
            <!-- <Button type="primary" size="small" style="margin-right: 5px" @click="show(index)">查看</Button> -->
            <Button type="error" size="small" @click="editcourse(index)">修改</Button>
            
            <!-- <Button type="error" size="small" @click="remove(index)">Delete</Button> -->
        </template>
    </Table>
    <p style="color:#87CEFA;font-weight:900;font-size:20px;margin-top:20px;">毕业生去向申请</p>
    <hr style=" height:2px;border:none;border-top:2px dotted #87CEFA;margin-bottom:20px;" />
    <Table border :columns="columnsdestination" :data="datadestination">
        <template slot-scope="{ row }" slot="name">
            <strong>{{ row.name }}</strong>
        </template>
        <template slot-scope="{ row, index }" slot="action">
            <!-- <Button type="primary" size="small" style="margin-right: 5px" @click="show(index)">查看</Button> -->
            <Button type="error" size="small" @click="editdestination(index)">修改</Button>
            
            <!-- <Button type="error" size="small" @click="remove(index)">Delete</Button> -->
        </template>
    </Table>
    <p style="color:#87CEFA;font-weight:900;font-size:20px;margin-top:20px;">考证信息申请</p>
    <hr style=" height:2px;border:none;border-top:2px dotted #87CEFA;margin-bottom:20px;" />
    <Table border :columns="columnscertification" :data="datacertification">
        <template slot-scope="{ row }" slot="name">
            <strong>{{ row.name }}</strong>
        </template>
        <template slot-scope="{ row, index }" slot="action">
            <!-- <Button type="primary" size="small" style="margin-right: 5px" @click="show(index)">查看</Button> -->
            <Button type="error" size="small" @click="editcertification(index)">修改</Button>
            
            <!-- <Button type="error" size="small" @click="remove(index)">Delete</Button> -->
        </template>
    </Table>
    
    </div>
  
</template>
<script>
export default {
  name: "Showinfo",
  data() {
    return {
    //   user_number:'',
      user_class: "",
      user_name: "",
      user_id: "",
      user_gender: "",
      user_password: "",
      user_number: "",
      user_type: "",
      databook: [],
    //   data: [],
      bookkey: [],
      datacourse: [],
    //   data: [],
      coursekey: [],
      datadestination: [],
    //   data: [],
      destinationkey: [],
      datacertification: [],
    //   data: [],
      certificationkey: [],
      columnscertification: [
                    // {
                    //     title: '学号',
                    //     slot: 'user_number'
                    // },
                    {
                        title: '证书名称',
                        key: 'certification_name'
                    },
                    {
                        title: '简介',
                        key: 'introduction'
                    },
                    {
                        title: '相关网站',
                        key: 'link'
                    },
                    {
                        title:'审核结果',
                        key: 'ischeck'
                    },
                    {
                        title: '操作',
                        slot: 'action',
                        width: 200,
                        align: 'center'
                    }
                ],
      columnscourse: [
                    // {
                    //     title: '学号',
                    //     slot: 'user_number'
                    // },
                    {
                        title: '课程名称',
                        key: 'course_name'
                    },
                    {
                        title: '教材',
                        key: 'book'
                    },
                    {
                        title: '类型',
                        key: 'type'
                    },

                    
                    {
                        title: '教师',
                        key: 'teacher'
                    },
                    {
                        title: '简介',
                        key: 'introduction'
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
      columnsbook: [
        // {
        //     title: '学号',
        //     slot: 'user_number'
        // },
        {
          title: "作者",
          key: "author",
        },
        {
          title: "书名",
          key: "book_name",
        },
        {
                        title: '类型',
                        key: 'type'
                    },
        {
          title: "简介",
          key: "introduction",
        },
        {
          title: "审核结果",
          key: "ischeck",
        },
        {
          title: "查看",
          slot: "action",
          width: 200,
          align: "center",
        },
      ],
      columnsdestination: [
                    // {
                    //     title: '学号',
                    //     slot: 'user_number'
                    // },
                    {
                        title: '姓名',
                        key: 'user_name'
                    },
                    {
                        title: '类型',
                        key: 'type'
                    },
                    {
                        title: '毕业去向',
                        key: 'destination_info'
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
    };
  },
  created() {
    // this.stu_num = window.sessionStorage.getItem("stu_num");


    this.user_number = window.sessionStorage.getItem("user_number");
    this.getstudentinfo();
    this.getallbook();
    this.getallcourse();
    this.getalldestination();
    this.getallcertification();
    // this.getbeevaluate();
    // this.getactivitygrade();
    // this.getmajorgrade();
    // this.calculate_sum()
  },
  methods: {
    getstudentinfo: function () {
      let self = this;
      self.$axios
        .get("/api/show_one_user/", {
          params: {
            user_number: self.user_number,
          },
        })
        .then((res) => {
          console.log(res.data.list);
          self.user_class = res.data.list[0].fields.user_class;
          self.user_name = res.data.list[0].fields.user_name;
          self.user_id = res.data.list[0].fields.user_id;
          self.user_gender = res.data.list[0].fields.user_gender;
          self.user_password = res.data.list[0].fields.user_password;
          if (self.user_class == "0") {
            self.user_type = "毕业生";
          } else if (self.user_class == "1") {
            self.user_type = "在校生";
          } else {
            self.user_type = "管理员";
          }
        });
    },
    show(index) {
      this.$Modal.info({
        title: "毕业去向",
        content: `姓名：${this.data[index].fields.user_name}<br>学号：${this.data[index].pk}<br>毕业去向：${this.data[index].fields.destination_info}`,
      });
    },
    getallbook() {
      let self = this;
      this.$axios
        .get("/api/show_someone_book/", {
          params: {
            user_number: self.user_number,
          },
        })
        .then((res) => {
          console.log(res.data);
        //   self.data = res.data.list;
          for (var i = 0; i < res.data.list.length; i++) {
            self.databook.push(res.data.list[i].fields);
            self.bookkey.push(res.data.list[i].pk);
          }
          //   self.data6 = res.data.list
          console.log(self.databook);
        });
    },
    getallcourse() {
      let self = this;
      this.$axios
        .get("/api/show_someone_course/", {
          params: {
            user_number: self.user_number,
          },
        })
        .then((res) => {
          console.log(res.data);
        //   self.data = res.data.list;
          for (var i = 0; i < res.data.list.length; i++) {
            self.datacourse.push(res.data.list[i].fields);
            self.coursekey.push(res.data.list[i].pk);
          }
          //   self.data6 = res.data.list
          console.log(self.datacourse);
        });
    },
    getalldestination() {
      let self = this;
      this.$axios
        .get("/api/show_someone_destination/", {
          params: {
            user_number: self.user_number,
          },
        })
        .then((res) => {
          console.log(res.data);
        //   self.data = res.data.list;
          for (var i = 0; i < res.data.list.length; i++) {
            self.datadestination.push(res.data.list[i].fields);
            self.destinationkey.push(res.data.list[i].pk);
          }
          //   self.data6 = res.data.list
          console.log(self.datadestination);
        });
    },
    getallcertification() {
      let self = this;
      this.$axios
        .get("/api/show_someone_certification/", {
          params: {
            user_number: self.user_number,
          },
        })
        .then((res) => {
          console.log(res.data);
        //   self.data = res.data.list;
          for (var i = 0; i < res.data.list.length; i++) {
            self.datacertification.push(res.data.list[i].fields);
            self.certificationkey.push(res.data.list[i].pk);
          }
          //   self.data6 = res.data.list
          console.log(self.datacertification);
        });
    },
    showbook (index) {
                this.$Modal.info({
                    title: '书籍信息',
                    content: 
                    `<Card>
                    名称：${this.data[index].certification_name}<br>
                    发布者：${this.data6[index].publisher}<br>
                    介绍：${this.data6[index].introduction}<br>
                    相关网站：${this.data6[index].link}
                    </Card>
                    `
                })
            },
    showcousrse (index) {
                this.$Modal.info({
                    title: '幕课信息',
                    content: 
                    `<Card>
                    名称：${this.data6[index].certification_name}<br>
                    发布者：${this.data6[index].publisher}<br>
                    介绍：${this.data6[index].introduction}<br>
                    相关网站：${this.data6[index].link}
                    </Card>
                    `
                })
            },
    showcertification (index) {
                this.$Modal.info({
                    title: '考证信息',
                    content: 
                    `<Card>
                    名称：${this.data6[index].certification_name}<br>
                    发布者：${this.data6[index].publisher}<br>
                    介绍：${this.data6[index].introduction}<br>
                    相关网站：${this.data6[index].link}
                    </Card>
                    `
                })
            },
    showdestination (index) {
                this.$Modal.info({
                    title: '考证信息',
                    content: 
                    `<Card>
                    名称：${this.data6[index].certification_name}<br>
                    发布者：${this.data6[index].publisher}<br>
                    介绍：${this.data6[index].introduction}<br>
                    相关网站：${this.data6[index].link}
                    </Card>
                    `
                })
            },
    editbook(index){
                this.k=this.bookkey[index]
                console.log(this.k)
                this.$router.push({
                    name:'EditBook',
                    params:{
                        book_id: this.k
                    }
                })
            },
    editcourse(index){
        this.k=this.coursekey[index]
        console.log(this.k)
        this.$router.push({
            name:'EditCourse',
            params:{
                course_id: this.k
            }
        })
    },
    editdestination(index){
        this.k=this.destinationkey[index]
        console.log(this.k)
        this.$router.push({
            name:'EditDestination',
            params:{
                user_number: this.k
            }
        })
    },
    editcertification(index){
        this.k=this.certificationkey[index]
        console.log(this.k)
        this.$router.push({
            name:'EditCertification',
            params:{
                certification_id: this.k
            }
        })
    },
    editinfo(){
        // this.k=this.certificationkey[index]
        // console.log(this.k)
        this.$router.push({
            name:'EditInfo'
        })
    }
  },
};
</script>
<style scoped>
.info {
  /* border-radius: 20px;
  border-style: solid;
  border-color: cornflowerblue; */
  width: 35%;
  padding-right: 2%;
  margin-left: 30%;
  margin-top: 2%;
  font-size: 15px;
}
/* .info {
  margin-left: 30%;
} */
</style>
