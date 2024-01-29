import { Component, OnInit } from '@angular/core';
import { EditorModule } from '@tinymce/tinymce-angular'
import {FormControl, FormGroup, ReactiveFormsModule} from '@angular/forms';
import { MatInputModule } from '@angular/material/input';
import { MatButton } from '@angular/material/button';
import { ChipsModule } from 'primeng/chips';
@Component({
  selector: 'app-create-post',
  standalone: true,
  imports: [EditorModule, ReactiveFormsModule, MatInputModule, MatButton, ChipsModule],
  templateUrl: './create-post.component.html',
  styleUrl: './create-post.component.scss'
})
export class CreatePostComponent implements OnInit {
  addPostForm!: FormGroup;
  title = new FormControl('');
  desc = new FormControl('');
  body = new FormControl('');
  values = new FormControl<string[] | null>(null);
  editorConfig = {
    base_url: '/tinymce',
    suffix: '.min',
    plugins: 'lists link image code table wordcount save',
    height: 650
  };
  ngOnInit(): void {
    this.addPostForm = new FormGroup({
      title: this.title,
      desc: this.desc,
      values: this.values,
      body: this.body
    });
  }
  addPost() {
    var obj: any= {};
    obj['content'] = this.addPostForm.get('body')!.value;
    console.log(obj);
    console.log(this.addPostForm.get('body')!.value);
    console.log(this.addPostForm.get('title')!.value);
    console.log(this.addPostForm.get('desc')!.value);
    console.log(this.addPostForm.get('values')!.value);
  }
}
