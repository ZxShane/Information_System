<template>
<div>
    <h1 align="center">幕课信息</h1>
    <hr>
    <List item-layout="vertical">
        <ListItem v-for="item in data" :key="item.pk">
            <ListItemMeta :title="item.fields.course_name" :description="item.fields.publisher" />
            <p>教师：{{ item.fields.teacher}}</p>
            <p>教材：{{ item.fields.book }}</p>
            <p>类型：{{ item.fields.type }}</p>
            <p>{{item.fields.introduction}}</p>
            <template slot="action">
                <li>
                    <Icon type="ios-star-outline" /> 123
                </li>
                <li>
                    <Icon type="ios-thumbs-up-outline" /> 234
                </li>
                <li>
                    <Icon type="ios-chatbubbles-outline" /> 345
                </li>
            </template>
            <template slot="extra">
                <img src="https://dev-file.iviewui.com/5wxHCQMUyrauMCGSVEYVxHR5JmvS7DpH/large" style="width: 280px">
            </template>
        </ListItem>
    </List>
</div>
</template>
<script>
    export default {
        name:'ShowBook',
        data () {
            return {
                data: [
                    // {
                    //     title: 'This is title 1',
                    //     description: 'This is description, this is description, this is description.',
                    //     avatar: 'https://dev-file.iviewui.com/userinfoPDvn9gKWYihR24SpgC319vXY8qniCqj4/avatar',
                    //     content: 'This is the content, this is the content, this is the content, this is the content.'
                    // },
                    // {
                    //     title: 'This is title 2',
                    //     description: 'This is description, this is description, this is description.',
                    //     avatar: 'https://dev-file.iviewui.com/userinfoPDvn9gKWYihR24SpgC319vXY8qniCqj4/avatar',
                    //     content: 'This is the content, this is the content, this is the content, this is the content.'
                    // },
                    // {
                    //     title: 'This is title 3',
                    //     description: 'This is description, this is description, this is description.',
                    //     avatar: 'https://dev-file.iviewui.com/userinfoPDvn9gKWYihR24SpgC319vXY8qniCqj4/avatar',
                    //     content: 'This is the content, this is the content, this is the content, this is the content.'
                    // }
                ]
            }
        },
        created(){
            this.getallcourse()
        },
        methods:{
          getallcourse:function(){
            let self = this
            this.$axios.get('/api/show_course/').then(res=>{
              console.log(res.data.list)
              self.data = res.data.list
            //   for(var i = 0;i<res.data.list.length;i++)
            //   {
            //     if(res.data.list[i].fields.ischeck){
            //       if(res.data.list[i].fields.isagree){
            //         res.data.list[i].fields.isagree = "通过"
            //       }else{
            //         res.data.list[i].fields.isagree = "未通过"
            //       }
            //     }else{
            //       res.data.list[i].fields.isagree = "未审核"
            //     }
            //     self.onestudent.stu_num = res.data.list[i].pk
            //     self.onestudent.scholar_name = res.data.list[i].fields.scholar_name
            //     self.onestudent.isagree = res.data.list[i].fields.isagree
            //     self.data1.push(self.onestudent)
            //   }
              
            })
          }
    }
    }
</script>
