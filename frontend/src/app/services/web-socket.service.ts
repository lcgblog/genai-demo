import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { webSocket, WebSocketSubject } from 'rxjs/webSocket';
@Injectable({
  providedIn: 'root'
})
export class WebSocketService {
  private positionSocket$: WebSocketSubject<any> | undefined;

  constructor(private http: HttpClient) { 
  }

  getPositions(topic: string, subscription: (value: any) => void): void {
    this.positionSocket$ = webSocket(`ws://localhost:8008/table/ws/${topic}`);
    this.positionSocket$.next({});
    this.positionSocket$.subscribe({
      next: (value: any) => {
        // Handle received value
        subscription(value);
      },
      error: (error: any) => {
        // Handle error
        console.error('WebSocket error:', error);
      },
      complete: () => {
        // Handle completion
        console.log('WebSocket connection closed');
      }
    });
  }

  addPosition(position: any): void {
    // Add your code here
    this.http.post('http://localhost:8008/table/addPosition', position).subscribe(
      response => {
        console.log('Position added:', response);
      }
    );
  }
}
