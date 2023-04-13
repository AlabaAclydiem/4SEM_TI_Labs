#ifndef CRYPTO_CLASSES_HPP
#define CRYPTO_CLASSES_HPP

class Cipher {
public:
    Cipher();
    void test();
};

class Algorithm {
public:
    static long long fastModuloPower();
    static std::vector <long long> allRoots();
    static std::pair <long long, long long> extendedEuclidea();
};

#endif