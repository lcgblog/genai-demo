// web-socket.service.ts
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { Client, Message, over } from 'webstomp-client';

@Injectable({
  providedIn: 'root'
})
export class WebSocketService {
  private stompClient: Client;
  private positionSubject: BehaviorSubject<any> = new BehaviorSubject(null);

  constructor() {
    console.log('WebSocketService creating');
    const socket = new WebSocket('ws://localhost:8080/ws');
    this.stompClient = over(socket);
    this.stompClient.connect({}, () => {
      this.onConnect();
    });  
  }

  private onConnect(): void {
    // Subscribe to the position topic
    this.stompClient.subscribe('/topic/fullPosition', (message: Message) => {
      this.positionSubject.next(JSON.parse(message.body));
    });
    console.log('WebSocketService connected');
  }

  // Send getPosition request
  public getPosition(): void {
    this.stompClient.send('/app/getFullPosition');
  }

  // Get position updates as an Observable
  public getPositionUpdates(): Observable<any> {
    return this.positionSubject.asObservable();
  }

  public disconnect(): void {
    if (this.stompClient) {
      this.stompClient.disconnect();
    }
  }
}
