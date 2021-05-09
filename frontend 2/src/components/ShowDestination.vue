<template>
<div>
<h1 align="center">毕业生去向汇总</h1>
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
                    title: '毕业去向',
                    content: `姓名：${this.data[index].fields.user_name}<br>学号：${this.data[index].pk}<br>毕业去向：${this.data[index].fields.destination_info}`
                })
            },
            remove (index) {
                this.data6.splice(index, 1);
            },
            getalldestination(){
            let self = this
            this.$axios.get('/api/show_destination/').then(res=>{
              console.log(res.data.list)
              self.data=res.data.list
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
