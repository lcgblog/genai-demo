package com.citi.onepx.genaidemo.demo.domain;

import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class Position {
    private String key;
    private String cusip;
    private String account;
    private Double netposition;
    private Double price;

    public Position(String key, String cusip, String account, Double netposition, Double price) {
        this.key = key;
        this.cusip = cusip;
        this.account = account;
        this.netposition = netposition;
        this.price = price;
    }
}
