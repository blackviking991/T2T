import { Component, Inject, Input } from '@angular/core';
import { Comment } from '../../model/Comment';
import { CommonModule, DatePipe } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { MatButtonModule } from '@angular/material/button';
import {
  MatDialog,
  MatDialogRef,
  MatDialogActions,
  MatDialogClose,
  MatDialogTitle,
  MatDialogContent,
  MAT_DIALOG_DATA,
} from '@angular/material/dialog';
import { MatInput } from '@angular/material/input';

@Component({
  selector: 'comments-section',
  standalone: true,
  imports: [HttpClientModule, DatePipe,FormsModule, CommonModule],
  templateUrl: './comments-section.component.html',
  styleUrl: './comments-section.component.scss'
})
export class CommentsSectionComponent {
  @Input() postId!: string;
  @Input() comments!: Comment[];
  
  http: HttpClient;
  desc: string;

  constructor(private httpClient: HttpClient, public dialog: MatDialog) {
    this.desc = "";
    this.http = httpClient;
  }

  pushComment(body: Comment) {
    if(body.text === "") return;
    this.http.post('http://localhost:8080/comments/add', body, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem("access_token")}`
      }
    }).subscribe((res: any) => {
      console.log(res);
      if(!this.comments) {
        this.comments = [body];
      } else {
        if(body.parentCommentId) {
          let index = this.comments.findIndex(com => com.cID === body.parentCommentId)
          if(index != -1) {
            let childComments = this.comments[index].childComments ?? [];
            childComments.push(res.comment);
            this.comments[index].childComments = childComments;
          }
        } else {
          this.comments.push(res.comment);
        }
      }
    },(err: any) => {
      console.log(err);
    });
  }

  addComment() {
    // cal API
    this.pushComment({
      text: this.desc,
      postId: this.postId
    });
    this.desc = "";
  }

  updateLike(cID: string) {
    this.http.get(`http://localhost:8080/comments/like/${cID}/${1}`, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem("access_token")}`
      }
    }).subscribe((res: any) => {
      console.log(res);
      this.comments = [ ...this.comments ];
    },(err: any) => {
      console.log(err);
    });
  }

  openDialog(cID: string): void {
    let dialogRef = this.dialog.open(DialogAnimationsExampleDialog, {
      width: '250px',
      data: { cID, pID: this.postId, http: this.http }
    });
    dialogRef.afterClosed().subscribe((res) => {
      // this.comments = [...this.comments];
      console.log('milgaaya', res);
      if(!this.comments) {
        this.comments = [res];
      } else {
        if(res.parentCommentId) {
          let index = this.comments.findIndex(com => com.cID === res.parentCommentId)
          if(index != -1) {
            let childComments = this.comments[index].childComments ?? [];
            childComments.push(res.comment);
            this.comments[index].childComments = childComments;
          }
        } else {
          this.comments.push(res.comment);
        }
      }
    });
  }

}

@Component({
  selector: 'dialog-animations-example-dialog',
  template: `<h1 mat-dialog-title>Comment</h1>
  <input matInput cdkFocusInitial style="margin: 5px;" (keydown.enter)="addChildComment()" [(ngModel)]="desc" />
  <div mat-dialog-actions>
    <button mat-button mat-dialog-close (click)="addChildComment()">Add</button>
  </div>`,
  standalone: true,
  imports: [MatInput,FormsModule, MatButtonModule, MatDialogActions, MatDialogClose, MatDialogTitle, MatDialogContent],
})
export class DialogAnimationsExampleDialog {

  desc!: string;
  cID!: string;
  pID!: string;
  http!: HttpClient;

  constructor(public dialogRef: MatDialogRef<DialogAnimationsExampleDialog>, @Inject(MAT_DIALOG_DATA) public data: {cID: string, pID: string, http: HttpClient}) {
    this.desc = "";
    this.cID = data.cID;
    this.pID = data.pID;
    this.http = data.http;
  }
  
  pushComment(body: Comment) {
    if(body.text === "") return;
    this.http.post('http://localhost:8080/comments/add', body, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem("access_token")}`
      }
    }).subscribe((res: any) => {
      console.log(res);
      setTimeout(() => {
        this.dialogRef.close(res.comment);
      }, 2000);
    },(err: any) => {
      console.log(err);
    });
  }

  addChildComment() {
    // call API
    this.pushComment({
      text: this.desc,
      postId: this.pID,
      parentCommentId: this.cID
    });
    this.desc = "";
  }
}

