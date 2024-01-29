import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import {MatButtonModule} from '@angular/material/button';
import {MatSidenavModule} from '@angular/material/sidenav';
@Component({
  selector: 'app-leader',
  standalone: true,
  imports: [MatSidenavModule, MatButtonModule],
  templateUrl: './leader.component.html',
  styleUrl: './leader.component.scss'
})
export class LeaderComponent implements OnInit{
  constructor(private http: HttpClient){}
  leaderBoard: any = [];
  ngOnInit(): void {
      this.http.get('http://localhost:8080/getLeaders').subscribe((data: any) => {
        console.log(data);
      },(err => {
        console.log(err);
      }))
  }
  showFiller = false;
}
