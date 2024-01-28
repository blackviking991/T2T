import { Routes } from '@angular/router';
import { HomePageComponent } from './components/home-page/home-page.component';
import { CreatePostComponent } from './components/create-post/create-post.component';
import { ViewPostComponent } from './components/view-post/view-post.component';
import { ProfilePageComponent } from './components/profile-page/profile-page.component';
import { ForumPageComponent } from './components/forum-page/forum-page.component';

export const routes: Routes = [
    { path: '', component: HomePageComponent },
    { path: 'profile', component: ProfilePageComponent },
    { path: 'forum/:name', component: ForumPageComponent },
    { 
        path: 'posts',
        children: [
            { path: 'create', component: CreatePostComponent },
            { path: ':id', component: ViewPostComponent }
        ]
    }
];
