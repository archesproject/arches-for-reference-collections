<script setup lang="ts">
import { inject } from "vue";
import type { Ref } from "vue";

import Button from "primevue/button";

import arches from "arches";

const resultsSelected = inject("resultsSelected") as Ref<string[]>;

const props = defineProps({
    searchResult: {
        type: Object,
        required: true,
    },
});

function selectResult(resourceid: string) {
    resultsSelected.value = [resourceid];
}

function clearResult() {
    resultsSelected.value = [];
}
</script>

<template>
    <section
        class="result"
        :class="{
            hovered: resultsSelected.includes(
                searchResult._source.resourceinstanceid,
            ),
        }"
        @mouseenter="selectResult(searchResult._source.resourceinstanceid)"
        @mouseleave="clearResult"
    >
        <div class="image-placeholder">
            <img src="https://picsum.photos/160" />
        </div>
        <div class="result-content">
            <h2>{{ props.searchResult._source.displayname }}</h2>
            <p class="breadcrumb">
                (North and Central America &gt; United States &gt; Missouri &gt;
                Greene)
            </p>
            <p class="scope-note">
                {{ searchResult._source.displaydescription }}
            </p>
            <div class="actions">
                <Button
                    label="...show more"
                    severity="secondary"
                    text
                />
                <Button
                    label="edit"
                    severity="secondary"
                    text
                    as="a"
                    target="_blank"
                    :href="'./' + arches.urls.resource + '/' + searchResult._id"
                />
            </div>
        </div>
    </section>
</template>

<style scoped>
.result {
    background-color: #fff;
    border: 1px solid #ddd;
    display: flex;
    flex-direction: row;
}
.result.hovered {
    background-color: rgb(239 245 252);
    border: 1px solid rgb(139 145 252);
}
.result .result-content {
    height: 16rem;
    overflow: hidden;
    padding-inline-start: 10px;
}
.result h2 {
    margin: 0 0 10px;
    font-size: 1.2rem;
}
.result .breadcrumb {
    color: #888;
    font-size: 0.9rem;
    margin-bottom: 10px;
}
.result .image-placeholder {
    width: 16rem;
    height: 16rem;
    min-width: 16rem;
    background-color: #eee;
}
.actions {
    display: flex;
    gap: 10px;
    margin-top: 10px;
}
</style>
