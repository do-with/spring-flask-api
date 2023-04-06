package com.example.demo.controller;

import org.springframework.ui.Model;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("/api")
public class ViewController {

    @GetMapping(value = "/view")
    public String getData(Model model) throws Exception {
        model.addAttribute("Data", GetDataController.getData());
        return "view";
    }
}