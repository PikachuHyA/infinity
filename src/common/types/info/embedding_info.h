//
// Created by JinHai on 2022/10/28.
//

#pragma once

#include "common/types/complex/embedding_type.h"
#include "common/types/type_info.h"

namespace infinity {

class EmbeddingInfo : public TypeInfo {
public:
    explicit EmbeddingInfo(EmbeddingDataType type, i64 dimension):
            TypeInfo(TypeInfoType::kEmbedding),
            embedding_type_(type),
            dimension_(dimension)
            {}

    ~EmbeddingInfo() override = default;

private:
    EmbeddingDataType embedding_type_{EmbeddingDataType::kInvalid};
    i64 dimension_;
};

}
