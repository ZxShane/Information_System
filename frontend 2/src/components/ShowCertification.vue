<template>
<div>
<h1 align="center">考证信息汇总</h1>
<Table border :columns="columns12" :data="data6">
    <template slot-scope="{ row }" slot="name">
        <strong>{{ row.name }}</strong>
    </template>
    <template slot-scope="{ row, index }" slot="action">
        <Button type="primary" size="small" style="margin-right: 5px" @click="show(index)">View</Button>
        <!-- <Button type="error" size="small" @click="remove(index)">Delete</Button> -->
    </template>
</Table>
</div>
</template>
<script>
    export default {
        data () {
            return {
                columns12: [
                    // {
                    //     title: '学号',
                    //     slot: 'user_number'
                    // },
                    {
                        title: '名称',
                        key: 'certification_name'
                    },
                    {
                        title: '发布者',
                        key: 'publisher'
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
                        title: '查看',
                        slot: 'action',
                        width: 150,
                        align: 'center'
                    }
                ],
                data:[],
                data6: [
                    // {
                    //     name: 'John Brown',
                    //     age: 18,
                    //     address: 'New York No. 1 Lake Park'
                    // },
                    // {
                    //     name: 'Jim Green',
                    //     age: 24,
                    //     address: 'London No. 1 Lake Park'
                    // },
                    // {
                    //     name: 'Joe Black',
                    //     age: 30,
                    //     address: 'Sydney No. 1 Lake Park'
                    // },
                    // {
                    //     name: 'Jon Snow',
                    //     age: 26,
                    //     address: 'Ottawa No. 2 Lake Park'
                    // }
                ]
            }
        },
        created(){
            this.getalldestination()
        },
        methods: {
            show (index) {
                this.$Modal.info({
                    title: '考证信息',
                    content: `名称：${this.data6[index].certification_name}<br>发布者：${this.data6[index].publisher}<br>介绍：${this.data6[index].introduction}<br>相关网站：${this.data6[index].link}`
                })
            },
            remove (index) {
                this.data6.splice(index, 1);
            },
            getalldestination(){
            let self = this
            this.$axios.get('/api/show_certification/').then(res=>{
              console.log(res.data.list)
            //   self.data=res.data.list
              for (var i =0;i<res.data.list.length;i++){
                  self.data6.push(res.data.list[i].fields)
              }
            //   self.data6 = res.data.list
            console.log(self.data6)
        })
        }
        }
    
    }
</script>
