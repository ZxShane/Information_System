<template>
<div>
<h1 align="center">书籍信息</h1>
    <hr>
    <List item-layout="vertical">
        <ListItem v-for="item in data" :key="item.pk">
            <ListItemMeta :title="item.fields.author+item.fields.book_name" :description="item.fields.publisher" />
            <p>类型：{{item.fields.type}}</p>
            <p>{{ item.fields.introduction }}</p>
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
                ]
            }
        },
        created(){
            this.getallbook()
        },
        methods:{
          getallbook:function(){
            let self = this
            this.$axios.get('/api/show_book/').then(res=>{
              console.log(res.data.list)
              self.data = res.data.list
           
              
            })
          }
    }
    }
</script>
