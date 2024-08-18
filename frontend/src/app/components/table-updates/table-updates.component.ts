import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { WebSocketService } from '../../services/web-socket.service';

@Component({
  selector: 'app-table-updates',
  templateUrl: './table-updates.component.html',
  styleUrls: ['./table-updates.component.css']
})
export class TableUpdatesComponent implements OnInit, OnDestroy {
  public tableData: any[] = [];
  private subscription: Subscription = new Subscription();

  constructor(private webSocketService: WebSocketService) {}

  ngOnInit(): void {
    this.webSocketService.sendMessage({ destination: '/app/getFullPosition' });

    const messageSubscription = this.webSocketService.getMessages().subscribe((message) => {
      if (message.destination === '/topic/fullPosition' || message.destination === '/topic/positionUpdates') {
        this.tableData = message.body;
      }
    });

    this.subscription.add(messageSubscription);
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }
}