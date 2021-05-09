import Vue from 'vue'
import Router from 'vue-router'

import Load from '@/components/Load'


import info from '@/components/info'

import PersonalInfo from '@/components/PersonalInfo'

import Showinfo from '@/components/Showinfo'
import ShowBook from '@/components/ShowBook'
import ShowCourse from '@/components/ShowCourse'
import ShowDestination from '@/components/ShowDestination'
import ShowCertification from '@/components/ShowCertification'
import ManageBook from '@/components/ManageBook'
import ManageCourse from '@/components/ManageCourse'
import ManageDestination from '@/components/ManageDestination'
import ManageCertification from '@/components/ManageCertification'
import EditBook from '@/components/Edit_Book'
import EditCourse from '@/components/Edit_Course'
import EditDestination from '@/components/Edit_Destination'
import EditCertification from '@/components/Edit_Certification'
import EditInfo from '@/components/Edit_Info'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Load',
      component: Load
    },
    
    {
      path: '/info',
      name: 'Info',
      component: info
    },
    {
      path:'/personalinfo',
      name:'PersonalInfo',
      component:PersonalInfo
    },
    {
      path:'/showinfo',
      name:'Showinfo',
      component:Showinfo
    },
    {
      path:'/showbook',
      name:'ShowBook',
      component: ShowBook
    },
    {
      path:'/showcourse',
      name:'ShowCourse',
      component: ShowCourse
    },
    {
      path:'/showdestination',
      name:'ShowDestination',
      component: ShowDestination
    },
    {
      path:'/showcertification',
      name:'ShowCertification',
      component: ShowCertification
    },
    {
      path:'/managebook',
      name: 'ManageBook',
      component:ManageBook
    },
    {
      path:'/managecourse',
      name: 'ManageCourse',
      component:ManageCourse
    },
    
    {
      path:'/managedestination',
      name: 'ManageDestination',
      component:ManageDestination
    },
    {
      path:'/managecertification',
      name: 'ManageCertification',
      component:ManageCertification
    }
    ,
    {
      path:'/editbook',
      name: 'EditBook',
      component:EditBook
    },
    {
      path:'/editcourse',
      name: 'EditCourse',
      component:EditCourse
    }
    ,
    {
      path:'/editdestination',
      name: 'EditDestination',
      component:EditDestination
    },
    {
      path:'/editcertification',
      name: 'EditCertification',
      component:EditCertification
    },
    {
      path:'/editinfo',
      name: 'EditInfo',
      component:EditInfo
    }
  ]
})


