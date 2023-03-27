package com.example.demo.Dto;

import com.example.demo.MyResource;
import lombok.AllArgsConstructor;
import lombok.Data;

import java.util.List;
import java.util.stream.Collectors;


import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class MyResourceDto {
    private String name;
    private String age;
    private String code;

}

