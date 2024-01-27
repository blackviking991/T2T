import { Routes } from '@angular/router';
import { HomePageComponent } from './components/home-page/home-page.component';
import { ForumPageComponent } from './components/forum-page/forum-page.component';
import { CreatePostComponent } from './components/create-post/create-post.component';
import { ProfilePageComponent } from './components/profile-page/profile-page.component';
export const routes: Routes = [
    {path: 'home', component: HomePageComponent},
    {path: '', redirectTo: '/home', pathMatch: 'full'},
    {path: 'forums', component: ForumPageComponent},
    {path: 'profile', component: ProfilePageComponent},
    {path: 'create-new', component: CreatePostComponent},

];
