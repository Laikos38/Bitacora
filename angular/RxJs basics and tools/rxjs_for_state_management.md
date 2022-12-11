# RxJs for state management

Lets say that our app it's going to manage some products data. We are going to have a service to provide that data to our componentes across the app.

So we will have something like this:

```typescript
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

export interface Products {
  code: number;
  name: string;
  active: boolean;
}

@Injectable({ providedIn: 'root' })
export class ProductService {
  private products$ = new BehaviorSubject<Products[]>([]);

  constructor(private http: HttpClient) {}
}
```

Why a `BehaviorSubject`?

Because unlike `Subject`, `BehaviorSubject` will always have an initial value and it will always return the last value when we subscribe to it.

Alright, now we create a method to access this stream:

```typescript
import { BehaviorSubject, Observable } from 'rxjs';

...
getProductsStream(): Observable<Products[]> {
    return this.products$.asObservable();
}
```

So, now we need to emit some data to the stream, lets suppouse that we have a refresh products method, that makes a HTTP request to the backend.

```typescript
refreshProductList(): void {
    this.http.get<Products[]>('.../products/').subscribe((products) => {
        this.products$.next(products);
    });
}
```

This way, anything that is subscribe to the Subject its gonna get those data update in real time as soon as the `next` method is triggered and react accordanly.

The components that needs to consume the stream should implements something like this:

```typescript
import { Component, OnDestroy, OnInit } from '@angular/core';
import { Observable, Subscription } from 'rxjs';
import { Products, ProductService } from '../../product.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit, OnDestroy {
  public products$: Observable<Products[]>;
  public productSubscription: Subscription;

  constructor(
    private productService: ProductService
  ) { }

  ngOnInit() {
    this.products$ = this.productService.getProductsStream();

    this.productSubscription = this.products$.subscribe(p => {
      console.log(p);
    });
  }

  ngOnDestroy() {
    this.productSubscription.unsubscribe();
  }
}
```

You can use the `async` pipe in the template instead of subscribing and unsubscribing.
