import { Component, OnInit } from '@angular/core';
import { EditorModule } from '@tinymce/tinymce-angular'
import {FormControl, FormGroup, ReactiveFormsModule, Validators} from '@angular/forms';
import { MatInputModule } from '@angular/material/input';
import { MatButton } from '@angular/material/button';
import { ChipsModule } from 'primeng/chips';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { DropdownModule } from 'primeng/dropdown';
import { Router } from '@angular/router';
@Component({
  selector: 'app-create-post',
  standalone: true,
  imports: [HttpClientModule,EditorModule,DropdownModule ,ReactiveFormsModule, MatInputModule, MatButton, ChipsModule],
  templateUrl: './create-post.component.html',
  styleUrl: './create-post.component.scss'
})
export class CreatePostComponent implements OnInit {
  constructor(private http: HttpClient, private router: Router){}

  addPostForm!: FormGroup;
  title = new FormControl('');
  shortDesc = new FormControl('');
  desc = new FormControl('');
  tags = new FormControl<string[] | null>(null);
  forumName = new FormControl<string[] | null>(null, Validators.required);
  forums: any = [];

  editorConfig = {
    base_url: '/tinymce',
    suffix: '.min',
    plugins: 'lists link image code table wordcount save',
    height: 650
  };
  ngOnInit(): void {
    this.addPostForm = new FormGroup({
      title: this.title,
      shortDesc: this.shortDesc,
      tags: this.tags,
      desc: this.desc,
      forumName: this.forumName
    });
    this.http.get('http://localhost:8080/forum/allForums').subscribe((res: any) =>{
        console.log(res);
        this.forums = res;
    }, ((err: any) => {
      console.log(err);
    }));
  }
  addPost() {
    console.log(this.addPostForm.value);
    var postBody: any = this.addPostForm.value;
    postBody.forumName = this.addPostForm.get('forumName')!.value['forumName'];
    console.log(this.addPostForm.get('desc')!.value);
    console.log(this.addPostForm.get('title')!.value);
    console.log(this.addPostForm.get('shortDesc')!.value);
    console.log(this.addPostForm.get('tags')!.value);
    console.log(this.addPostForm.get('forumName')!.value);
    this.http.post('http://localhost:8080/posts/add', postBody,
    {headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${localStorage.getItem("access_token")}`}
    })
    .subscribe((res: any) =>{
      console.log(res);
      window.alert("Post successfully created! Redirecting to profile")
    }),((err: any) => {
      console.log(err);
    });
    setTimeout(() => {
      this.router.navigate(['/profile']);
    }, 3000);

  }
}
